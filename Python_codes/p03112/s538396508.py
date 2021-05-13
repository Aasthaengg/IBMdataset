import bisect

A, B, Q = map(int, input().split())

INF=10**18
S=[-INF]+[int(input()) for i in range(A)]+[INF]
T=[-INF]+[int(input()) for i in range(B)]+[INF]

for i in range(Q):
    x = int(input())
    s = bisect.bisect_left(S, x)
    t = bisect.bisect_left(T, x)
    saisyo = float("inf")
    for j in [S[s], S[s-1]]:
        for k in [T[t], T[t-1]]:
            saisyo = min(saisyo, abs(j-x)+abs(k-j), abs(k-x)+abs(j-k))
    print(saisyo)