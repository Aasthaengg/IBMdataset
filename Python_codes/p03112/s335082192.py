from bisect import bisect_right
A, B, Q = map(int, input().split())
INF = float('inf')
S = [-INF] + [int(input()) for _ in range(A)] + [INF]
T = [-INF] + [int(input()) for _ in range(B)] + [INF]
X = [int(input()) for _ in range(Q)]
for x in X:
    b, d =  bisect_right(S, x), bisect_right(T, x)
    ans = INF
    for s in [S[b - 1], S[b]]:
        for t in [T[d - 1], T[d]]:
            d1, d2 = abs(s - x) + abs(s - t), abs(t - x) + abs(s - t)
            ans = min(ans, d1, d2)
    print(ans)