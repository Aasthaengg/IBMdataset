#高速化heapqダイクストラ
from collections import *
from heapq import*
import sys
input=lambda:sys.stdin.readline()


def DIJKSTRA(point,d):
    cost      = [float("inf")]*(n+1)
    Q         = []
    cost[point]=0
    heappush(Q,(point,cost[point]))
    while Q:
        prefnd,tmpC=heappop(Q)
        if cost[prefnd]<tmpC:
            continue
        for node,c in d[prefnd]:
            altC=c+tmpC
            if cost[node]>altC:
                cost[node]=altC
                heappush(Q,(node,altC))
    return cost

n=int(input())
d={}
for i in range(n-1):
    a,b=map(int,input().split())
    if a in d.keys():
        d[a].append([b,1])
    else:
        d[a]=[[b,1]]
    if b in d.keys():
        d[b].append([a,1])
    else:
        d[b]=[[a,1]]
        
x=DIJKSTRA(1,d)[1:]
y=DIJKSTRA(n,d)[1:]
#print(x)
#print(y)
F=0
S=0
for i in range(n):
    if x[i]<=y[i]:
        F+=1
    else:
        S+=1
if F<=S:
    print("Snuke")
else:
    print("Fennec")