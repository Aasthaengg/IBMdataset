H,W = list(map(int,input().split()))
N=10

dist = []
for n in range(N):
    dist.append(list(map(int,input().split())))
dist=[list(x) for x in zip(*dist)]

from collections import deque
start = 1

color = {}
for n in range(N):
    color[n] = -1
    
cost = {}
for n in range(N):
    cost[n] = 10**10
    
parent = {}
for n in range(N):
    parent[n] = -1

cost[start] = 0
S = deque([])
while True:
    mincost = 10**10
    for n in range(N):
        if color[n] != 1 and cost[n] < mincost:
            mincost = cost[n]
            start = n
    
    if mincost == 10**10:
        break
    
    color[start] = 1
    
    for n in range(N):
        if color[n] != 1 and dist[start][n] != -1:
            if cost[start] + dist[start][n] < cost[n]:
                cost[n] = cost[start] + dist[start][n]
                parent[n] = start
                color[n] = 0

cost[-1]=0
ans=0
for h in range(H):
    W = list(map(int,input().split()))
    for w in W:
        ans += cost[w]
print(ans)