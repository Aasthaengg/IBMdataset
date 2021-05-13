import sys
from bisect import bisect_left
from collections import defaultdict
def input(): return sys.stdin.readline().strip()

def main():
    H, W, N = map(int, input().split())
    black = []
    d = defaultdict(list)
    for _ in range(N):
        a, b = map(int, input().split())
        black.append((a - 1, b - 1))
        d[a - 1].append(b - 1)
    for key in d: d[key].sort()

    ans = [0] * 10
    checked = set()
    # (a, b)がテンプレートのどこにいるかで９通り試す
    for i in range(9):
        for a, b in black:
            h, w = a - i // 3, b - i % 3
            if (h, w) in checked: continue
            if h < 0 or w < 0: continue
            if h > H - 3 or w > W - 3: continue
            cnt = 0
            idx1 = bisect_left(d[h], w)
            idx2 = bisect_left(d[h], w + 3)
            cnt += idx2 - idx1
            idx1 = bisect_left(d[h + 1], w)
            idx2 = bisect_left(d[h + 1], w + 3)
            cnt += idx2 - idx1
            idx1 = bisect_left(d[h + 2], w)
            idx2 = bisect_left(d[h + 2], w + 3)
            cnt += idx2 - idx1
            #print("({}, {})=>{}".format(h, w, cnt))
            ans[cnt] += 1
            checked.add((h, w))
    ans[0] = (H - 2) * (W - 2) - sum(ans[1:])
    for a in ans: print(a)




if __name__ == "__main__":
    main()
