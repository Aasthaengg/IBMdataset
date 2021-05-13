from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s, t = map(int, input().split())

dist = [[-3] * 3 for _ in range(n+1)]
dist[s][0] = 0

q = deque([(s, 0)])

while q:
    now, c = q.popleft()
    ne = (c+1) % 3
    for node in graph[now]:
        if dist[node][ne] != -3:
            continue
        dist[node][ne] = dist[now][c] + 1
        q.append((node, ne))

print(dist[t][0] // 3)
