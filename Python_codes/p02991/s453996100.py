from collections import deque

inf = float('inf')

n, m = map(int, input().split())

es = [[] for _ in range(n * 3)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    es[u].append(v + n)
    es[u + n].append(v + n * 2)
    es[u + n * 2].append(v)

s, t = map(int, input().split())
s -= 1
t -= 1

dq = deque()
dq.append(s)

can = False
dist = [inf] * (n * 3)
dist[s] = 0

while dq:
    v = dq.popleft()
    if v == t:
        can = True
        break
    for nv in es[v]:
        if dist[nv] == inf:
            dq.append(nv)
            dist[nv] = dist[v] + 1

if not can:
    print(-1)
else:
    print(dist[t] // 3)
