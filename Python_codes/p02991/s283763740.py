#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,m=map(int,input().split())
G=[[] for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    u-=1; v-=1
    G[u].append(v)
s,t=map(int,input().split())
s-=1; t-=1

# dp=[[inf]*3 for i in range(n)]
# dp[s][0] = 0

def disktra(g,s):
    n=len(g)
    dist = [[inf]*3 for i in range(n)]
    dist[s][0] = 0
    hq=collections.deque(); hq.appendleft((0,s))
    while hq:
        cost,u =hq.pop()
        if dist[u][cost%3] < cost:
            continue
        for v in g[u]:
            if dist[v][(dist[u][cost%3]+1)%3] <= dist[u][cost%3] + 1:
                continue
            dist[v][(dist[u][cost%3]+1)%3] = dist[u][cost%3] + 1
            hq.appendleft((dist[v][(dist[u][cost%3]+1)%3],v))
    return dist

dp=disktra(G,s)
print(-1 if dp[t][0]==inf else dp[t][0]//3)
# print(*dp,sep="\n")