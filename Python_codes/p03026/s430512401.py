from heapq import heappush, heappop
def dijkstra(graph:list, node:int, start:int) -> list:
    # graph[node] = [(cost, to)]
    inf = float('inf')
    dist = [inf]*node

    dist[start] = 0
    heap = [(0,start)]
    while heap:
        cost,thisNode = heappop(heap)
        for NextCost,NextNode in graph[thisNode]:
            dist_cand = dist[thisNode]+NextCost
            if dist_cand < dist[NextNode]:
                dist[NextNode] = dist_cand
                heappush(heap,(dist[NextNode],NextNode))
    return dist

N = int(input())

e = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append((1,b))
    e[b].append((1,a))

c = list(map(int,input().split()))
c.sort()
print(sum(c)-c[-1])
d = dijkstra(e,N,0)
d = [(d[i],i) for i in range(N)]
d.sort()
d = [(d[i][0],d[i][1],c[-i-1]) for i in range(N)]
d.sort(key=lambda x:x[1])
ans = [str(d[i][2]) for i in range(N)]
print(' '.join(ans))