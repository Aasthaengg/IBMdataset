from bisect import bisect_left

INF = 2 * 10**10

A, B, Q = map(int, input().split())
S = [-INF] + [int(input()) for _ in range(A)] + [INF]
T = [-INF] + [int(input()) for _ in range(B)] + [INF]
X = [int(input()) for _ in range(Q)]
ans = []
for x in X:
    sr = bisect_left(S, x) 
    sl = sr if S[sr] == x else sr -1
    tr = bisect_left(T, x)
    tl = tr if T[tr] == x else tr -1

    ll = x - min(S[sl], T[tl])
    rr = max(S[sr], T[tr]) - x
    lsrt = 2*(x-S[sl]) + (T[tr] - x)
    ltrs = 2*(x-T[tl]) + (S[sr] - x)
    rslt = 2*(S[sr] - x) + (x - T[tl])
    rtls = 2*(T[tr] - x) + (x - S[sl])

    ans.append(min(ll, rr, lsrt, ltrs, rslt, rtls))
print(*ans, sep='\n')