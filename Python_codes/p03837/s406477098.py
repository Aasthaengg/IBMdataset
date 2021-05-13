N, M = map(int, input().split())
edges_used = {}

from heapq import heappush, heappop
def dijkstra(n, graph, s):
    dist = [float('inf')] * n
    hq = [(0, s)]
    dist[s] = 0
    while hq:
        c, v = heappop(hq)
        if dist[v] < c:
            continue
        for t, cost in graph[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(hq, (dist[t], t))
    return dist

graph = [[] for _ in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))
    edges_used[(a, b, c)] = False
dist = [dijkstra(N, graph, i) for i in range(N)]

for edge in edges_used.keys():
    a, b, c = edge
    for i in range(N):
        if dist[i][a] == dist[i][b] + c or dist[i][b] == dist[i][a] + c:
            edges_used[edge] = True

ans = 0
for used in edges_used.values():
    if not used:
        ans += 1
print(ans)