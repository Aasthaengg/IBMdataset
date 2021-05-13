# C - /\/\/\/

from collections import defaultdict
import sys
readline = sys.stdin.readline

n = int(readline())
v = list(int(x) for x in readline().split())

d0 = defaultdict(int)
d1 = defaultdict(int)
d0[0] = 0
d1[0] = 0
for i in range(n):
    if i%2:
        d1[v[i]] += 1
    else:
        d0[v[i]] += 1

d0 = list(d0.items())
d1 = list(d1.items())
d0.sort(key=lambda x: x[1], reverse=True)
d1.sort(key=lambda x: x[1], reverse=True)

if d0[0][0] != d1[0][0]:
    ans = n - d0[0][1] - d1[0][1]
else:
    ans = n - max(d0[0][1] + d1[1][1], d0[1][1] + d1[0][1])
print(ans)