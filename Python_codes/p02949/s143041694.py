import sys


def input():
    return sys.stdin.readline()[:-1]


n, m, p = map(int, input().split())
edge0 = []
d = [[] for i in range(n)]
r = [[] for i in range(n)]
for i in range(m):
    ai, bi, ci = map(int, input().split())
    edge0.append((bi-1,ai-1,-ci+p))
    d[ai-1] += [bi-1]
    r[bi-1] += [ai-1]

p0 = [False for i in range(n)]
p0[0] = True
from collections import deque
q = deque([0])
while len(q)>0:
    x = q.popleft()
    for y in d[x]:
        if not p0[y]:
            p0[y] = True
            q.append(y)
pn = [False for i in range(n)]
pn[n-1] = True
q = deque([n-1])
while len(q) > 0:
    x = q.popleft()
    for y in r[x]:
        if not pn[y] and p0[y]:
            pn[y] = True
            q.append(y)

edge = []
for e in edge0:
    if pn[e[1]] and pn[e[0]]:
        edge += [e]


dist = [float("inf") for i in range(n)]
dist[n-1] = 0
h = False
for i in range(n):
    updated = False
    for e in edge:
        if dist[e[1]] > dist[e[0]] + e[2] and p0[e[1]] and p0[e[0]]:
            dist[e[1]] = dist[e[0]] + e[2]
            updated = True
    if not updated:
        break
else:
    h = True

if h:
    print(-1)
else:
    print(max(0, -dist[0]))
