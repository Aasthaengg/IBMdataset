from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
data = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    data.append([a - 1, b - 1])

ans = 0

def dfs(queue, a, b):
    while len(queue) != 0:
        x = queue.popleft()
        for i in range(len(graph[x])):
            if (min(graph[x][i], x) != a or max(x, graph[x][i]) != b) and visited[graph[x][i]] == 0:
                queue.append(graph[x][i])
                visited[graph[x][i]] = 1

for i in range(m):
    visited = [0] * n
    visited[0] = 1
    queue = deque()
    queue.append(0)
    dfs(queue, data[i][0], data[i][1])
    if sum(visited) != n:
        ans += 1

print(ans)