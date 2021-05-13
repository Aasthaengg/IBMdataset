import sys
input = sys.stdin.readline
n, m, p = map(int, input().split())
edges = []
forward_edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, p-c))
    forward_edges[a].append(b)


can_reach = [0]*n
stack = [0]
while stack:
    v = stack.pop()
    if can_reach[v]:
        continue
    can_reach[v] = 1
    for v2 in forward_edges[v]:
        if can_reach[v2]:
            continue
        stack.append(v2)


INF = 10**10
dist = [INF]*n
dist[0] = 0
for i in range(n):
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
    print(-1)
else:
    print(max(0, -dist[-1]))