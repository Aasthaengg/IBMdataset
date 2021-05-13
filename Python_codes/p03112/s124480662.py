import sys
input = sys.stdin.readline
import bisect

a,b,q = map(int, input().split())
INF = 10**18
s = [-INF] + [int(input()) for _ in range(a)] + [INF]
t = [-INF] + [int(input()) for _ in range(b)] + [INF]
for _ in range(q):
    x = int(input())
    i = bisect.bisect_right(s,x)
    j = bisect.bisect_right(t,x)
    d = INF
    for si in [s[i-1],s[i]]:
        for ti in [t[j-1],t[j]]:
            d1 = abs(x-si)+abs(ti-si)
            d2 = abs(x-ti)+abs(ti-si)
            d = min(d,d1,d2)
    print(d)