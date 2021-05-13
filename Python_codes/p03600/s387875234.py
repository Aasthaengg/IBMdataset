import heapq
from collections import deque

N = int(input())
A = [[int(a) for a in input().split()] for _ in range(N)]

def dijkstra_heap(s, edge, n):
    #始点sから各頂点への最短距離
    d = [10**9+1] * n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d


Road = [[] for _ in range(N)]
h = []
for i in range(N):
    for j in range(i+1, N):
        heapq.heappush(h, (A[i][j], i, j))
        
m = h[0][0]
D = [[10**9+1]*N for _ in range(N)]
ans = 0
while h:
    t = heapq.heappop(h)
    cost = t[0]
    i = t[1]
    j = t[2]
    if cost < 2*m:
        Road[i].append((cost, j))
        Road[j].append((cost, i))
        D[i][j] = cost
        D[j][i] = cost
    elif D[i][j] > cost:
        D[i] = dijkstra_heap(i, Road, N)
        if D[i][j] > cost:
            Road[i].append((cost, j))
            Road[j].append((cost, i))
            D[i][j] = cost
            D[j][i] = cost
    if D[i][j] < cost:
        ans = -1
        break
            
if ans == 0:
    for i in range(N):
        for t in Road[i]:
            ans += t[0]
            
    ans //= 2
        
print(ans)