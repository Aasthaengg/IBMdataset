import heapq
from itertools import permutations
def dijkstra(n, tc_edges, s):
    
    min_dist = [float('inf')] * n
    min_dist[s] = 0
    next_v = []
    heapq.heappush(next_v, (0, s))
    
    while True:
        if len(next_v) == 0: break
        d, v = heapq.heappop(next_v)
        
        for u, d in tc_edges[v]:
            if min_dist[u] > min_dist[v] + d:
                min_dist[u] = min_dist[v] + d
                heapq.heappush(next_v, (min_dist[u], u))
                
    return min_dist
    
n, m, r = map(int, input().split())
r = list(map(int, input().split()))
edge = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a-1].append([b-1, c])
    edge[b-1].append([a-1, c])

dist = [dijkstra(n, edge, i) for i in range(n)]

ans = float('inf')
for pr in permutations(r):
    temp = 0
    for i in range(len(r)-1):
        temp += dist[pr[i]-1][pr[i+1]-1]
        if temp >= ans: break
    
    ans = min(ans, temp)
    
print(ans)