N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
deg = [0] * (N+1)
for i in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    deg[y] += 1
G[0] = list(range(1, N+1))
for i in range(1,N+1):
    deg[i] += 1

from collections import deque
topo = [0]
deq = deque(topo)

while deq:
    v = deq.popleft()
    for t in G[v]:
        deg[t] -= 1
        if deg[t] == 0:
            topo.append(t)
            deq.append(t)

dp = [-1] * (N+1)
for v in topo:
    for t in G[v]:
        dp[t] = max(dp[t], dp[v] + 1)

print(max(dp))