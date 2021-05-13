#transit tree path
n=int(input())
graph={i:{} for i in range(1,n+1)}
for i in range(n-1):
    a,b,d=map(int,input().split())
    graph[a][b]=d
    graph[b][a]=d

import heapq
def dijkstra(s,graph,n):
    dist=[10**20 for i in range(n+1)]
    dist[s]=0
    pq=[]
    heapq.heapify(pq)
    heapq.heappush(pq,(0,s))
    while pq:
        x=heapq.heappop(pq)
        node,mini_dis=x[1],x[0]
        for point in graph[node].keys():
            w=graph[node][point]
            newlen=dist[node]+w
            if newlen<dist[point]:
                heapq.heappush(pq,(newlen,point))
                dist[point]=newlen
    return dist
Q,K=map(int,input().split())
P=dijkstra(K,graph,n)
for i in range(Q):
    x,y=map(int,input().split())
    print(P[x]+P[y])  