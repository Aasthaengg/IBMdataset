n=int(input())
es=[[] for _ in range(n)]

for _ in range(n-1):
    a,b,c=map(int,input().split())
    es[a-1].append((b-1,c))
    es[b-1].append((a-1,c))

from heapq import heappush, heappop
def dijkstra(edges, size, source):
    distance = [float('inf')] * size
    distance[source] = 0
    visited = [False] * size
    pq = []
    heappush(pq, (0, source))
    while pq:
        dist_v, v = heappop(pq)
        visited[v] = True
        for u, weight in edges[v]:
            if not visited[u]:
                new_dist = dist_v + weight
                if distance[u] > new_dist:
                    distance[u] = new_dist
                    heappush(pq, (new_dist, u))
    return distance


q,k=map(int,input().split())
k-=1
dist=dijkstra(es,n,k)
for _ in range(q):
    x,y=map(int,input().split())
    x-=1
    y-=1
    print(dist[x]+dist[y])