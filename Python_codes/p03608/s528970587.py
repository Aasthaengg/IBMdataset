N,M,R= list(map(int,input().split()))
towns = list(map(int,input().split()))
for i in range(R):
    towns[i] += -1

G = [[] for i in range(N)]
for i in range(M):
    A,B,C = list(map(int,input().split()))
    G[A-1].append([C,B-1]) #重み、向かう先の順番
    G[B-1].append([C,A-1])

dists = [[float("inf")]*N for i in range(R)]

import heapq

for i in range(R):
    town = towns[i]
    dist = dists[i]
    dist[town] = 0
    used = [0]*N
    used[town] = 1

    nextlist = []
    for next in G[town]:
        heapq.heappush(nextlist,next)

    while len(nextlist):
        minnext = heapq.heappop(nextlist)
        if used[minnext[1]]==1:
            continue
        v = minnext[1]
        dist[v] = minnext[0]
        used[v] = 1
        for next in G[v]:
            if used[next[1]]==0:
                heapq.heappush(nextlist,[next[0]+dist[v],next[1]])

from itertools import permutations
townorders = list(permutations(towns))

out = float("inf")
for townorder in townorders:
    cand = 0
    for i in range(R-1):
        now = townorder[i]
        nowind = towns.index(now)
        next = townorder[i+1]
        cand += dists[nowind][next]
    if cand<out:
        out=cand
print(out)
