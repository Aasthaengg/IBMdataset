import sys
from bisect import bisect_left
from bisect import bisect_right
input = sys.stdin.readline
a,b,q = map(int, input().split())
INF = 10**20
ss = [-INF] + [int(input()) for i in range(a)] + [INF]
ts = [-INF] + [int(input()) for i in range(b)] + [INF]
xs = [int(input()) for i in range(q)] 

ans = INF
for x in xs:
    si = bisect_left(ss, x)
    ti = bisect_left(ts, x)

    dist1 = abs(x-ss[si-1]) + 2*abs(x-ts[ti])
    dist2 = 2*abs(x-ss[si-1]) + abs(x-ts[ti])
    dist3 = abs(x-ts[ti-1]) + 2*abs(x-ss[si])
    dist4 = 2*abs(x-ts[ti-1]) + abs(x-ss[si])
    dist5 = max(abs(x-ss[si-1]), abs(x-ts[ti-1]))
    dist6 = max(abs(x-ss[si]), abs(x-ts[ti]))
    dist = min(dist1,dist2,dist3,dist4,dist5,dist6)
    # print(dist,"du",x,dist1,dist2,dist3,dist4,dist5,dist6)
    print(dist)


