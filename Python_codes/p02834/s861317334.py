import sys
input = sys.stdin.readline

n, u, v = [int(x) for x in input().split()]

import heapq
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

################################
n, w = n, n - 1 #n:頂点数　w:辺の数

edge = [[] for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(w):
    x,y = map(int,input().split())
    z = 1
    edge[x - 1].append([z,y - 1])
    edge[y - 1].append([z,x - 1]) 

takahashi = dijkstra_heap(u - 1)
aoki = dijkstra_heap(v - 1)

ans = takahashi[v - 1] - 1 # 高橋君がいもる

idx = 0
for i, j in zip(takahashi, aoki):
    if idx == u - 1 or idx == v - 1:
        idx += 1
        continue
    if j - i > 0:
        ans = max(ans, j - 1)
    idx += 1

print(ans)