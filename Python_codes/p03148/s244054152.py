import sys
input = sys.stdin.readline
from collections import *
from heapq import *

N, K = map(int, input().split())
td = [tuple(map(int, input().split())) for _ in range(N)]
td.sort(key=lambda t: t[1], reverse=True)
d = defaultdict(list)
now = 0

for ti, di in td[:K]:
    d[ti].append(di)
    now += di

remove = []

for k in d.keys():
    d[k].sort(reverse=True)
    
    for i in range(1, len(d[k])):
        heappush(remove, d[k][i])
    
s = set(list(d.keys()))
add = []

for ti, di in td:
    if ti in s:
        continue
    
    s.add(ti)
    heappush(add, -di)

x = len(d)
ans = now+x**2

while len(remove)>0 and len(add)>0:
    now -= heappop(remove)
    now -= heappop(add)
    x += 1
    ans = max(ans, now+x**2)

print(ans)