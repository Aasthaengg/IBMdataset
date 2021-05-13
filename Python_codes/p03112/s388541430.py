from bisect import bisect_left

A, B, Q = map(int, input().split())
INF = 10**12
s = [-INF] + [int(input()) for _ in range(A)] + [INF]
t = [-INF] + [int(input()) for _ in range(B)] + [INF]

for _ in range(Q):
    x = int(input())
    si = bisect_left(s,x)
    ti = bisect_left(t,x)
    sl = [s[si-1],s[si]]
    tl = [t[ti-1],t[ti]]
    ans = INF
    for i in range(2):
        for j in range(2):
            ans = min(ans, abs(x-sl[i])+abs(sl[i]-tl[j]), abs(x-tl[j])+abs(tl[j]-sl[i]))
    print(ans)