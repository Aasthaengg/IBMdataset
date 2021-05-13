from collections import deque, defaultdict

N, M = map(int, input().split())
edge = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    edge[(a, 0)].append((b, 1))
    edge[(a, 1)].append((b, 2))
    edge[(a, 2)].append((b, 0))

S, T = map(int, input().split())

inf = float('inf')
dist = {}
for i in range(1, N+1):
    dist[(i, 0)] = inf
    dist[(i, 1)] = inf
    dist[(i, 2)] = inf
dist[(S, 0)] = 0

dq = deque()
dq.append((S, 0))

while dq:
    v = dq.popleft()
    if v == (T, 0):
        break
    for u in edge[v]:
        if dist[u] < inf: continue
        dq.append(u)
        dist[u] = dist[v] + 1

if(dist[(T, 0)] == inf):
    print(-1)
else:
    print(dist[(T, 0)]//3)
