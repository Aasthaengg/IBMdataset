from collections import deque

inf = float('inf')

n, m = map(int, input().split())

g = [set() for _ in range(n * 3)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].add(v + n)
    g[u + n].add(v + n * 2)
    g[u + n * 2].add(v)

s, t = map(int, input().split())
s -= 1
t -= 1

dq = deque()
dq.append(s)

dist = [inf] * (n * 3)
dist[s] = 0
while dq:
    v = dq.popleft()
    if v == t:
        break
    for u in g[v]:
        if dist[u] < inf: continue
        dq.append(u)
        dist[u] = dist[v] + 1

if dist[t] == inf:
    print(-1)
else:
    print(dist[t] // 3)
