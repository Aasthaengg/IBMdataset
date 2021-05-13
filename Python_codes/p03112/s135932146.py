from bisect import bisect_left

INF = 2 * 10**10

A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]
ans = []
for x in X:
    sr = bisect_left(S, x) 
    sl = sr -1
    if sr != len(S) and S[sr] == x:
        sl = sr
    tr = bisect_left(T, x)
    tl = tr - 1
    if tr != len(T) and T[tr] == x:
        tl = tr

    ll = INF if sl == -1 or tl == -1 else x - min(S[sl], T[tl])
    rr = INF if sr == len(S) or tr == len(T) else max(S[sr], T[tr]) - x
    lsrt = INF if sl == -1 or tr == len(T) else 2*(x-S[sl]) + (T[tr] - x)
    ltrs = INF if tl == -1 or sr == len(S) else 2*(x-T[tl]) + (S[sr] - x)
    rslt = INF if tl == -1 or sr == len(S) else 2*(S[sr] - x) + (x - T[tl])
    rtls = INF if sl == -1 or tr == len(T) else 2*(T[tr] - x) + (x - S[sl])

    ans.append(min(ll, rr, lsrt, ltrs, rslt, rtls))
print(*ans, sep='\n')