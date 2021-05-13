import heapq
def dijkstra_heap(s,g):
    used = [True] * n #True:未確定
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,[e[0],e[1]])
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        if v==g:
            return minedge[0]
        kai=minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,[e[0]+kai,e[1]])                   
    return -1

################################
n,m = map(int,input().split()) #n:頂点数　w:辺の数

edge = [[] for i in range(n)]
#edge[i] : iから出る道の[重み,行先]の配列
pp=[]
for i in range(m):
    x,y,z = map(int,input().split())
    edge[x-1].append([z,y-1])
    edge[y-1].append([z,x-1])
    pp.append([x-1,y-1,z])
ans=0
for i in range(m):
    if pp[i][2]>dijkstra_heap(pp[i][0],pp[i][1]):
        ans+=1
print(ans)
