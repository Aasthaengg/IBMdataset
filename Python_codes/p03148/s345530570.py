import sys
input = sys.stdin.readline
from collections import *

N, K = map(int, input().split())
td = [tuple(map(int, input().split())) for _ in range(N)]
td.sort(key=lambda t: t[1], reverse=True)
d = defaultdict(list)
now = 0

for ti, di in td[:K]:
    d[ti].append(di)
    now += di

rem = []

for k in d.keys():
    d[k].sort(reverse=True)
    
    for i in range(1, len(d[k])):
        rem.append(d[k][i])

add = []
s = set()

for ti, di in td[K:]:
    if ti not in d and ti not in s:
        add.append(di)
        s.add(ti)

rem.sort()
add.sort(reverse=True)
var = len(list(d.keys()))
ans = now+var**2

for i in range(min(len(rem), len(add))):
    now -= rem[i]
    now += add[i]
    ans = max(ans, now+(var+i+1)**2)

print(ans)