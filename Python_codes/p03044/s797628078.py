# -*- coding: utf-8 -*-
#D - Even Relation
import sys 
from heapq import heappush, heappop
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())

edges = [[] for _ in range(N+1)]
INF = 10**31
dist = [INF]*(N+1) #最短距離用
prev=[None]*(N+1) #最短経路用
for _ in range(N-1):
  x,y,t = map(int, readline().split())
  edges[x].append((y,t))
  edges[y].append((x,t))
  
q = [(0,1)]
dist[1] = 0 #最短経路用
while q:
  cost, v = heappop(q)
  if dist[v] < cost:
    continue
  for vert,_cost in edges[v]:
    newcost = cost+_cost
    if newcost < dist[vert]:
      prev[vert] = v
      dist[vert] = newcost #最短経路用
      heappush(q,(newcost,vert))

for i in range(1,N+1):
    if dist[i] % 2 == 0:
        print(0)
    else:
        print(1)