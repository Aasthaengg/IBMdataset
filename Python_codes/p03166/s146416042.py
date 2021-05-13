from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]
deg = [0 for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    G[x].append(y)
    deg[y] += 1

stack = []

for u in range(N):
    if deg[u] == 0:
        stack.append(u) #入次数が0のノードをスタックに入れる
topol = []
while len(stack) != 0:
    u = stack.pop()
    topol.append(u)
    for v in G[u]:
        deg[v] -= 1
        if deg[v] == 0:
            stack.append(v)


dp = [0 for i in range(N)]
for u in topol:
    for v in G[u]:
        dp[v] = max(dp[v], dp[u]+1)
res = 0
for i in range(N):
    if res < dp[i]:
        res = dp[i]
print(res)