ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
import collections
import math
import itertools
import heapq as hq
import sys
n,m = ma()
G = [[]for i in range(3*n)]
for i in range(m):
    u,v = ma();u-=1;v-=1
    G[3*u].append(3*v+1)
    G[3*u+1].append(3*v+2)
    G[3*u+2].append(3*v)
s,t = ma()
s=(s-1)*3
t=(t-1)*3
visited=[False]*(3*n)
INF=10**9
dist = [INF]*(3*n)
que = collections.deque()
que.append(s)
visited[s]=True
dist[s]=0
while que:
    prev = que.popleft()
    for nex in G[prev]:
        if not visited[nex]:
            visited[nex]=True
            dist[nex]=dist[prev]+1
            que.append(nex)
if dist[t]==INF:
    print(-1)
else:
    print(dist[t]//3)
