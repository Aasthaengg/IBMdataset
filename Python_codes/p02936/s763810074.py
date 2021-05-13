from collections import deque

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
PX = [tuple(map(int, input().split())) for _ in range(Q)]
counter = [0] * (N + 1)
for px in PX:
    p, x = px
    counter[p] += x

q = deque()
visited = [-1] * (N+1)
visited[1] = 1
q.append(1)

while q:
    parent = q.pop()
    nodes = graph[parent]
    for node in nodes:
        if visited[node] == -1:
            visited[node] = 1
            q.append(node)
            counter[node] += counter[parent]

for i in range(1, N+1):
    print(counter[i], end=' ')