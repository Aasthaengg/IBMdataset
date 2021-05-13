import heapq
n = int(input())
edge = [[] for _ in range(n)]
for i in range(n-1):
  a,b,c = map(int,input().split())
  a-=1;b-=1 #0index
  edge[a].append([c,b])
  edge[b].append([c,a])
#print(edge)
Q,K = map(int,input().split())
K-=1 #0index

#d = [INF for _ in range(N)]
#d[K] = 0

def dijkstra_heap(s):
    #始点sから各頂点への最短距離
    d = [float("inf")] * n
    used = [True] * n #True:未確定。始点として探索されたか。というかdが更新されたか。
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中からスタートから最小の距離のものを探す
        if not used[minedge[1]]: #すでに探索済みの場合にはスキップして次のプライオリティーキューへ。
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False #ここで始点として探索済みにする。
        for e in edge[v]:
            if used[e[1]]: #行き先がすでに始点として探索済みでない場合には値を更新。
                heapq.heappush(edgelist,[e[0]+d[v],e[1]]) #重みをスタートからの最短重みにするため+d[v]
    return d ##始点sから各頂点への最短距離がアウトプットとなる。

d = dijkstra_heap(K)
#print(d)
for i in range(Q):
  x,y = map(int,input().split())
  x-=1;y-=1
  ans = d[x]+d[y]
  print(ans)