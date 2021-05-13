from collections import deque

N, Q = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N - 1)]
Y = [list(map(int, input().split())) for _ in range(Q)]

tree = [0] * (N + 1)
for p, x in Y:
    tree[p] += x

graph = [[] for _ in range(N + 1)]
for a, b in X:
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
visited[1] = True
stack = deque()
stack.append(1)
while stack:
    u = stack.popleft()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            tree[v] += tree[u]
            stack.append(v)
            
print(*tree[1:])
