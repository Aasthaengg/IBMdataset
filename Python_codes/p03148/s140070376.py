import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dt = []
for _ in range(n):
    a,b = map(int, input().split())
    dt.append([b,a])
dt.sort(reverse=True)
# print(dt)

t = [0] * (n+1)
from heapq import *

h = []
h2 = []
f = [0] * (n+1)
g = [0] * (n+1)
c = 0
tf = 0
for i in range(k):
    tmp = dt[i]
    if t[tmp[1]] == 0:
        t[tmp[1]] += 1
        c += 1
    else:
        heappush(h, tmp[0])
    tf += tmp[0]
f[c] = tf

for i in range(k, n):
    tmp = dt[i]
    if t[tmp[1]] == 0:
        t[tmp[1]] += 1
        heappush(h2, -tmp[0])

while len(h2) > 0 and len(h) > 0:
    tout = heappop(h)
    tin = -heappop(h2)
    c += 1
    tf = tf - tout + tin
    f[c] = tf

for i in range(n+1):
    ff = f[i]
    if ff != 0:
        g[i] = ff + i*i
print(max(g))
