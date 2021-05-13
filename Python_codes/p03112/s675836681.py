from bisect import bisect_left


A,B,Q = map(int, input().split())
INF = float("inf")
S = [int(input()) for _ in range(A)]
S = [-INF] + S + [INF]
T = [int(input()) for _ in range(B)]
T = [-INF] + T + [INF]
X = [int(input()) for _ in range(Q)]

ans = []
for x in X:
    idx_s = bisect_left(S, x)
    idx_t = bisect_left(T, x)
    candidate = [max(abs(x - T[idx_t - 1]), abs(x - S[idx_s-1])),
                max(abs(x - S[idx_s]), abs(x - T[idx_t])),
                2*abs(x - S[idx_s-1]) + abs(x - T[idx_t]),
                2*abs(x - T[idx_t]) + abs(x - S[idx_s-1]),
                2*abs(x - T[idx_t-1]) + abs(x - S[idx_s]),
                2*abs(x - S[idx_s]) + abs(x - T[idx_t-1])
                ]
    ans.append(min(candidate))

print(*ans, sep="\n")