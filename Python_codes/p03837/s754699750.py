import heapq
n,m, = map(int,input().split())
E = [[] for i in range(n)]
for i in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    E[a].append((c,b))
    E[b].append((c,a))


def dijkstra(x):
    dis = [float("inf")]*n
    dis[x] = 0
    q = []
    heapq.heappush(q,(0,x))
    
    while q:
        cost,bef = heapq.heappop(q)

        if dis[bef] < cost:
            continue

        for ncost,nex in E[bef]:
            dist = ncost+cost

            if dist < dis[nex]:
                dis[nex] = dist
                heapq.heappush(q,(dist,nex))
    return dis

short = []
for i in range(n):
    short.append(dijkstra(i))
count = 0
for i in range(n):
    for dist,nex in E[i]:
        if short[i][nex] < dist:
            count += 1
print(count//2)

