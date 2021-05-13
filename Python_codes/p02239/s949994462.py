from collections import deque

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] += list(map(lambda x: x - 1, list(map(int, input().split()))[2:]))

visited = [-1] * n
que = deque()
# 頂点0を入れておく
que.append(0)
visited[0] = 0
cnt = 0

while que:
    v = que.popleft()
    for nv in graph[v]:
        if not visited[nv] == -1:
            continue
        visited[nv] = visited[v] + 1
        que.append(nv)

for v, d in enumerate(visited, 1):
    print(v, d)
