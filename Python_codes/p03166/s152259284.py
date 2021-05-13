from collections import deque

n,m = map(int,input().split())


grafo = [[] for i in range(n+1)]

num_adj = [0] * (n+1)

for i in range(m):
    u, v = map(int,input().split())
    grafo[u].append(v)
    num_adj[v] += 1

q = deque()

for i in range(1, n+1):
    if num_adj[i] == 0:
        q.append(i)

dp = [0] * (n + 1)

while q:
    n = q.popleft()
    for s in grafo[n]:
        num_adj[s] -= 1

        if num_adj[s] == 0:
            q.append(s)
            dp[s] = dp[n] + 1

print(max(dp))
