import heapq
def dijkstra(n, edge, dist, s):
    min_dist = [float('inf')] * n
    min_dist[s] = 0
    next_v = []
    heapq.heappush(next_v, (0, s))
    path = [-1] * n
    
    while True:
        if len(next_v) == 0: break
        d, v = heapq.heappop(next_v)
        
        for u in edge[v]:
            if min_dist[u] > min_dist[v] + dist[v][u]:
                min_dist[u] = min_dist[v] + dist[v][u]
                heapq.heappush(next_v, (min_dist[u], u))
                path[u] = v
                
    return min_dist, path

n, m = map(int, input().split())
dist = [[float('inf') for _ in range(n)] for _ in range(n)]
edge = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c

for i in range(n): dist[i][i] = 0

e = set()
for i in range(n):
    md, path = dijkstra(n, edge, dist, i)
    for i, p in enumerate(path):
        if p == -1: continue
        if i <= p: e.add((i, p))
        else: e.add((p, i))

print(m - len(e))