from collections import deque

n = int(input())
graph = []

for _ in range(n):
    u = list(map(int, input().split()))

    if u[1] == 0:
        graph.append([])
    else:
        graph.append(list(map(lambda x: x - 1, u[2: u[1] + 2])))

dist = [-1] * n


def bfs(x):
    q = deque([])
    dist[x] = 0
    q.append(x)

    while q:
        x = q.popleft()

        for nx in graph[x]:
            if dist[nx] != -1:
                continue
            else:
                dist[nx] = dist[x] + 1
                q.append(nx)


bfs(0)

for i in range(n):
    print(i + 1, dist[i])

