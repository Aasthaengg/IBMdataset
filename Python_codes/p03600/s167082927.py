ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys

n = ni()
cost =[]
tot = 0
for i in range(n):
    A = lma()
    cost.append(A)
    tot+=sum(A)
nu=[[False]*n for i in range(n)]
for k in range(n):
    for i in range(n):
        if i==k:continue
        for j in range(n):
            if j==k:
                continue
            #print("ijk",i,j,k,"cost",cost[i][j],cost[i][k]+cost[k][j])
            if cost[i][j] >cost[i][k] + cost[k][j]:
                print(-1)
                exit()
            elif cost[i][j]==cost[i][k] + cost[k][j]:

                nu[i][j]=True
#print(nu)
for i in range(n):
    for j in range(n):
        if nu[i][j]:
            tot-=cost[i][j]
print(tot//2)
