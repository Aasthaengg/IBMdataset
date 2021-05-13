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
n,c = ma()
INF=10**18
xv = []
for i in range(n):
    xv.append(lma())
xvr=xv[::-1]

ans=0
v1=0
v2=0
cost1=[0]*(n+1) #cost[i] ::iまで来た時の最大gain(戻る分を含む)
cost2=[0]*(n+1) #反時計回り
for i in range(n):
    v1 += xv[i][1]
    cost1[i]=max(v1-2*xv[i][0],cost1[i-1])
    v2+=xvr[i][1]
    cost2[i]=max(v2-2*(c-xvr[i][0]),cost2[i-1])
tmp=0
# print(cost1,cost2)
for i in range(n):
    tmp+=xv[i][1]
    #print(tmp,cost2[n-i-1])
    ans = max(ans, cost2[n-i-2] +tmp-xv[i][0] )
tmp=0
for i in range(n):
    tmp+=xvr[i][1]
    #print(tmp,cost1[n-i-1])
    ans = max(ans, cost1[n-i-2] +tmp-(c-xvr[i][0]) )

print(ans)
