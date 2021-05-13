#!/usr/bin/env python3
import sys, math, itertools, collections, bisect, heapq
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,m=map(int,input().split())
G=[[] for i in range(3*n)]
for i in range(m):
    u,v=map(int,input().split())
    u-=1; v-=1
    G[3*u].append(3*v+1)
    G[3*u+1].append(3*v+2)
    G[3*u+2].append(3*v)
s,t=map(int,input().split())
s-=1; t-=1

# dp=[[inf]*3 for i in range(n)]
# dp[s][0] = 0

def disktra(g,s):
    c=1
    n=len(g)
    dist = [inf]*n
    dist[s] = 0
    hq=[]
    heapq.heappush(hq,(dist[s],s))
    while hq:
        cost,u =heapq.heappop(hq)
        if dist[u] < cost:
            continue
        for v in g[u]:
            if dist[v] <= dist[u] +c:
                continue
            dist[v] = dist[u] + c
            heapq.heappush(hq,(dist[v],v))
    return dist

dp=disktra(G,3*s)
print(-1 if dp[3*t]==inf else dp[3*t]//3)
# print(*dp,sep="\n")