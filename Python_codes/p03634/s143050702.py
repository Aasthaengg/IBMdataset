import heapq
def dijkstra_heap(s):
    #始点sから各頂点への最短距離
    d = [float("inf")] * N
    used = [True] * N #True:未確定
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

N = int(input())

edge = [[] for i in range(N)]  # edge[i] : iから出る道の[重み,行先]の配列
for i in range(N-1):
    x,y,z = map(int,input().split())
    edge[x-1].append([z,y-1])
    edge[y-1].append([z,x-1])

Q, K = map(int, input().split())

zk = dijkstra_heap(K-1)
#print(zk)

for _ in range(Q):
    x, y = map(int, input().split())
    print(zk[x-1] + zk[y-1])
