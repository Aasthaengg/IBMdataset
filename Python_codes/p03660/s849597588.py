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

# n,w = map(int,input().split()) #n:頂点数　w:辺の数
n = int(input()) #n:頂点数　w:辺の数
w = n - 1

edge = [[] for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(w):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    edge[x].append([1,y])
    edge[y].append([1,x]) 

d0 = dijkstra_heap(0)
d1 = dijkstra_heap(n-1)

f = 0
s = 0
for i in range(1,n-1):
    if d0[i] <= d1[i]:
        f +=1
    else:
        s += 1

if f > s:
    print('Fennec')
else:
    print('Snuke')
    


