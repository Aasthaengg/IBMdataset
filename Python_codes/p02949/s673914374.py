ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
def BF(graph,s):##Bellman-Ford
    n=len(graph)
    INF=10**15
    dist = [INF]*n
    dist[s] = 0
    for _ in range(n-1):
        for u in range(n):
            if dist[u]==INF:
                continue
            for v,c in graph[u]:
                if dist[v] >dist[u]+c:
                    dist[v] =dist[u]+c
    for _ in range(n):
        for u in range(n):
            if dist[u]==INF:
                continue
            for v,c in graph[u]:
                if dist[v] >dist[u]+c:
                    dist[v]=-INF
    return dist
n,m,p  = ma()
G = [[] for i in range(n)]
for i in range(m):
    a,b,c = ma()
    G[a-1].append((b-1,-c+p))##コストが高いほうがいいので反転させておく
d=BF(G,0)
if abs(d[-1])==10**15:
    print(-1)
else:
    print(max(0,-d[-1]))
