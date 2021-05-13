
from collections import deque

N = int(input())
X = [list(map(int, input().split())) for _ in range(N - 1)]

graph = [[] for _ in range(N + 1)]
for u, v, w in X:
    graph[u].append((v, w))
    graph[v].append((u, w))

colors = [-1] * (N + 1)
colors[1] = 0
q = deque([1])
while q:
    u = q.popleft()
    for v, w in graph[u]:
        if colors[v] >= 0:
            continue

        if w % 2 == 0:
            colors[v] = colors[u]
        else:
            colors[v] = 1 - colors[u]
        q.append(v)

print(*colors[1:], sep="\n")
