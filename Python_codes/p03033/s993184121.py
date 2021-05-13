import bisect
import sys

sys.setrecursionlimit(10000)
INF = float('inf')

N, Q = list(map(int, next(sys.stdin).split()))
STX = [list(map(int, next(sys.stdin).split())) for _ in range(N)]
D = [int(next(sys.stdin)) for _ in range(Q)]

ans = [-1] * Q
nexts = [-1] * Q

for s, t, x in sorted(STX, key=lambda stx: (stx[2], stx[1])):
    # [lo, hi) に出発した人は x で止まる
    # x の小さい順にソート済みなのでここで確定
    lo = max(0, bisect.bisect_left(D, s - x))
    hi = min(len(D), bisect.bisect_left(D, t - x))

    p = lo
    while p < hi:
        if nexts[p] == -1:
            ans[p] = x
            nexts[p] = hi
            p += 1
        else:
            prev = p
            p = nexts[p]
            nexts[prev] = hi

print('\n'.join(map(str, ans)))
