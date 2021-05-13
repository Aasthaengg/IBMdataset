import bisect
A, B, Q = map(int,input().split())
s = [-10**20] + [int(input()) for k in range(A)] + [10**20,10**20]
t = [-10**20] + [int(input()) for k in range(B)] + [10**20,10**20]

for _ in range(Q):
    x = int(input())
    S = bisect.bisect_left(s,x)
    T = bisect.bisect_left(t,x)
    print(min(
        max(s[S],t[T])-x,
        x-min(s[S-1],t[T-1]),
        s[S]-x + s[S]-t[T-1],
        t[T]-x + t[T]-s[S-1],
        x-s[S-1] + t[T]-s[S-1],
        x-t[T-1] + s[S]-t[T-1]))
