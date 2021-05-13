import sys
input=sys.stdin.readline
from heapq import *
from collections import defaultdict
x, y, z, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a = sorted(a, reverse = True)
b = sorted(b, reverse = True)
c = sorted(c, reverse = True)

ans = [[-(a[0] + b[0] + c[0]), 0, 0, 0]]
heapify(ans)
log = defaultdict(lambda :0)

d = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
for i in range(k):
    temp, s, t, u = heappop(ans)
    temp = temp * (-1)
    print(temp)
    for ds, dt, du in d:
        ns = s + ds
        nt = t + dt
        nu = u + du
        if not(0 <= ns < x and 0 <= nt < y and 0 <= nu < z):continue
        if log[(ns, nt, nu)]:continue
        heappush(ans, [-(a[ns] + b[nt] + c[nu]), ns, nt, nu])
        log[(ns, nt, nu)] = 1
