from bisect import bisect_left
A, B, Q = map(int,input().split())
INF = 2 * 10 ** 10
S = [-INF]
T = [-INF]
for _ in range(A):
    S.append(int(input()))
S.append(INF)
for _ in range(B):
    T.append(int(input()))
T.append(INF)
for _ in range(Q):
    x = int(input())
    s = bisect_left(S, x)
    t = bisect_left(T, x)
    ans = min(max(S[s], T[t]) - x, x - min(S[s-1], T[t-1]), 2 * S[s] - T[t-1] - x, 2 * T[t] - S[s-1] - x, T[t] + x - 2 * S[s-1], S[s] + x - 2 * T[t-1])
    print(ans)