#高速化heapqダイクストラ
from collections import *
from heapq import*
import sys
input=lambda:sys.stdin.readline()


def BFS(point,d):
    cost=[1e7]*(n+1)
    cost[point]=0
    Q=[]
    heappush(Q,(0,point))
    
    while Q:
        c,p=heappop(Q)
        for np in d[p]:
            if cost[np]==1e7:
                cost[np]=c+1
                heappush(Q,(c+1,np))
    return cost

n=int(input())
d={}
for i in range(n-1):
    a,b=map(int,input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a]=[b]
    if b in d:
        d[b].append(a)
    else:
        d[b]=[a]
        
x=BFS(1,d)[1:]
y=BFS(n,d)[1:]

#print(x,y)

F=0
S=0

for s,t in zip(x,y):
    if s<=t:
        F+=1
    else:
        S+=1

if F<=S:
    print("Snuke")
else:
    print("Fennec")
