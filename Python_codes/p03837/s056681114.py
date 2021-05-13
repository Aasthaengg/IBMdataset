# -*- coding: utf-8 -*-
import sys 
from heapq import heappush, heappop
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

V,E = map(int, readline().split())
edges = [[] for _ in range(V+1)]

INF = 10**31

for _ in range(E):
    x,y,t = map(int, readline().split())
    edges[x].append((t,y))
    edges[y].append((t,x))
    

def dijkstra(q,dist,prev):
    while q:
        cost, v_from = heappop(q)
        if dist[v_from] < cost:
            continue
        for _cost,v_to in edges[v_from]:
            newcost = cost+_cost
            if newcost < dist[v_to]:
                prev[v_to] = v_from
                dist[v_to] = newcost #最短経路用
                heappush(q,(newcost,v_to))

pp = []
for i in range(1,V+1): 
    for j in range(i+1,V+1):
        dist = [INF]*(V+1) #最短距離用
        dist[i] = 0 #最短経路用
        prev=[None]*(V+1) 
        q = [(0,i)]
        dijkstra(q,dist,prev)
        p = [j]
        while prev[p[-1]]!=None:
            x,y = p[-1],prev[p[-1]]
            if x > y:
                x,y = y,x
            pp.append((x,y))
            p.append(prev[p[-1]])

print(E - len(set(pp)))