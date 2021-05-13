import heapq
def dijkstra_heap(s,edge):
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

import sys
input = sys.stdin.readline
n = int(input())
edge = [[] for i in range(n)]
for i in range(n-1):
    x,y,z = map(int,input().split())
    edge[x-1].append([z,y-1]) # list限定
    edge[y-1].append([z,x-1]) 

q,k = map(int,input().split())
chk = dijkstra_heap(k-1,edge)
  

for i in range(q):
  x,y = [int(i) for i in input().split()] 
  print(chk[x-1] + chk[y-1])