import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
deg = [0 for _ in range(N)]
dp = [0 for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    deg[y - 1] += 1

stack = []

for i in range(N):
    if not deg[i]:
        stack.append(i)

while stack:
    node = stack.pop()
    for adj in graph[node]:
        deg[adj] -= 1
        dp[adj] = max(dp[adj], dp[node] + 1)
        if not deg[adj]:
            stack.append(adj)

print(max(dp))