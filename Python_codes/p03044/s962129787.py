import numpy as np
from scipy.sparse.csgraph import shortest_path
import heapq
n = int(input())
edge = [[] for i in range(n)]
for i in range(n-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append([w, v])
    edge[v].append([w, u])

def dijkstra_heap(s):
    #始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,[e[0]+d[v],e[1]])
    return d

Path_from_0 = dijkstra_heap(0)
for i in range(n):
    print(Path_from_0[i] % 2)

