import heapq

N,u,v = map(int,input().split())
u -= 1
v -= 1

du = [float('inf')]*N
dv = [float('inf')]*N
G = [[]]*N

def calcDist(s, dist):
    q = []
    heapq.heappush(q,[0, s])
    dist[s] = int(0)
    
    while q!=[]:
        p = heapq.heappop(q)
        pv = p[1]
        if dist[pv] < p[0] :
            continue
        for eto in G[pv]:
            if dist[eto] > dist[pv] + 1:
                 dist[eto] = int(dist[pv] + 1)
                 heapq.heappush(q, [dist[eto], eto])


for i in range(N-1):
    e1,e2 = map(int, input().split())
    e1 -= 1
    e2 -= 1
    if G[e1] == []:
        G[e1] = [e2]
    else:
        G[e1].append(e2)
    if G[e2] == []:
        G[e2] = [e1]
    else:
        G[e2].append(e1)

if v in G[u]:
    ans = 0
else:    

    calcDist(v,dv)
    calcDist(u,du)
    maxD = 0
    for idu,idv in zip(du,dv):
        if idu < idv:
            maxD = max(maxD, idv)       
    ans = maxD-1
    
print(ans)