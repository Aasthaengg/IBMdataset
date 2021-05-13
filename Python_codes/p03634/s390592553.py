N = int(input())
import heapq
def dijkstra_heap(s):
    d = [float("inf")] * N
    used = [True] * N
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,[e[0]+d[v],e[1]])
    return d


edge = [[] for i in range(N)]
for i in range(N-1):
    x,y,z = map(int,input().split())
    edge[x-1].append([z,y-1])
    edge[y-1].append([z,x-1])
Q, K = map(int, input().split())
result = dijkstra_heap(K-1)
for i in range(Q):
    x, y = map(int, input().split())
    print(abs(result[x-1]-result[K-1])+abs(result[y-1]+result[K-1]))