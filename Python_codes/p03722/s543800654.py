n, m = map(int, input().split())
edges = []
forward_edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, -c))
    forward_edges[a].append(b)

stack = [0]
can_reach = [0]*n
while stack:
    v = stack.pop()
    if can_reach[v]:
        continue
    can_reach[v] = 1
    for v2 in forward_edges[v]:
        if can_reach[v2]:
            continue
        stack.append(v2)

INF = 10**18
dist = [INF]*n
dist[0] = 0
for i in range(n-1):
    for v, v2, c in edges:
        if dist[v2] <= dist[v]+c:
            continue
        dist[v2] = dist[v]+c

negative = [0]*n
for i in range(n):
    for v, v2, c in edges:
        if dist[v2] <= dist[v]+c:
            continue
        if not can_reach[v2]:
            continue
        dist[v2] = -INF
        negative[v2] = 1


if negative[-1]:
    print('inf')
else:
    print(-dist[-1])