import sys
# sys.setrecursionlimit(100000)
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def main():
    h, w, m = [int(i) for i in input().split()]
    d_h = defaultdict(int)
    d_w = defaultdict(int)
    bom = set()
    for _ in range(m):
        h, w = [int(i) for i in input().split()]
        bom.add((h, w))
        d_h[h] += 1
        d_w[w] += 1
    H = sorted(d_h.items(), key=lambda x: -x[1])
    W = sorted(d_w.items(), key=lambda x: -x[1])
    ans = 0
    for k_h, v_h in H:
        for k_w, v_w in W:
            tmp = v_h + v_w
            if (k_h, k_w) in bom:
                tmp -= 1
                ans = max(tmp, ans)
            else:
                ans = max(tmp, ans)
                break
        else:
            continue
        break

    for k_w, v_w in W:
        for k_h, v_h in H:
            tmp = v_h + v_w
            if (k_h, k_w) in bom:
                tmp -= 1
                ans = max(tmp, ans)
            else:
                ans = max(tmp, ans)
                break
        else:
            continue
        break
    print(ans)


if __name__ == "__main__":
    main()
