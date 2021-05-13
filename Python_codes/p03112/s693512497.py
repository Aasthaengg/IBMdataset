A,B,Q = map(int,input().split())
INF = 10**18
S = [-INF] + [int(input()) for _ in range(A)] + [INF]

T = [-INF] + [int(input()) for _ in range(B)] + [INF]

X = [int(input()) for _ in range(Q)]

from bisect import bisect_left

for _ in range(Q):
    ans = INF
    x = X[_]
    idxs = bisect_left(S, x)
    idxt = bisect_left(T, x)
    for s in [S[idxs-1], S[idxs]]:
        for t in [T[idxt-1], T[idxt]]:
            d1, d2 = abs(s-x) + abs(t-s), abs(t-x) + abs(s-t)
            ans = min(ans, d1, d2)
    print(ans)

