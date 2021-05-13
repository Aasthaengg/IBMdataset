from collections import deque
n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    deg[y] += 1

q = deque()

for i in range(1, n + 1):
    if deg[i] == 0:
        q.append(i)

dp = [0] * (n + 1)
while q:
    n = q.popleft()
    for zzz in g[n]:
        deg[zzz] -= 1
        if deg[zzz] == 0:
            q.append(zzz)
            dp[zzz] = dp[n] + 1

print(max(dp))
