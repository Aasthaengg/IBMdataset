import sys
from collections import defaultdict

def get_rect_pos(a, b):
    pos = []
    for i in range(3):
        for j in range(3):
            pos.append((a-i, b-j))

    return pos


def main():
    input = sys.stdin.readline
    H, W, N = map(int, input().split())
    d = defaultdict(lambda: 0)
    for _ in range(N):
        a, b = map(int, input().split())
        pos = get_rect_pos(a, b)
        for p in pos:
            if p[0] <= 0 or p[0] + 2 > H or p[1] <= 0 or p[1] + 2 > W:
                continue

            d[p] += 1

    ans = [0 for _ in range(10)]
    for key in d.keys():
        i = d[key]
        ans[i] += 1

    ans[0] = (H - 2) * (W - 2) - sum(ans)

    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
