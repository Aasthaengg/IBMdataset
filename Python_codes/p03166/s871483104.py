n, m = map(int, input().strip().split())
graph = {i:[] for i in range(1, n+1)}

deg = [0 for i in range(n+1)]
for i in range(m):
    v1, v2 = map(int, input().strip().split())
    graph[v1].append(v2)
    deg[v2] += 1

Q = []
for i in range(1, n+1):
    if deg[i] == 0:
        Q.append(i)

dp = [0 for i in range(n+1)]

while len(Q):
    curr = Q.pop()
    for i in graph[curr]:
        dp[i] = max(dp[i], dp[curr]+1)
        deg[i] -= 1
        if deg[i] == 0:
            Q.append(i)

print(max(dp))