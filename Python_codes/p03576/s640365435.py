import sys
from collections import *
import heapq
import math
import bisect
import copy
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,k=map(int,input().split())
xy=[list(map(int,input().split())) for i in range(n)]
ru=[[0]*(n+1) for i in range(n+1)]
lst=sorted(xy)
lst2=sorted(xy,key=lambda x: x[1])

for i in range(n):
    for j in range(n):
        flag=0
        for l in range(n):
            if xy[l]==[lst[i][0],lst2[j][1]]:
                flag=1
        if flag:
            ru[i+1][j+1]=1
        ru[i+1][j+1]+=ru[i+1][j]+ru[i][j+1]-ru[i][j]
# print(ru)
xdic=defaultdict(int)
ydic=defaultdict(int)
for i in range(n):
    xdic[lst[i][0]]=i+1
    ydic[lst2[i][1]]=i+1
# print(xdic)
# print(ydic)
lst=[0]*n
lst2=[0]*n
for i in range(n):
    x,y=xy[i]
    lst[i],lst2[i]=x,y
lst,lst2=list(permutations(lst,2)),list(permutations(lst2,2))
ans=float('inf')
for i in range(len(lst)):
    xl,xr=min(lst[i]),max(lst[i])
    for j in range(len(lst2)):
        yl,yr=min(lst2[j]),max(lst2[j])
        # print(ru[xdic[xr]][ydic[yr]]-ru[xdic[xr]][ydic[yl]-1]-ru[xdic[xl]-1][ydic[yr]]+ru[xdic[xl]-1][ydic[yl]-1])
        if ru[xdic[xr]][ydic[yr]]-ru[xdic[xr]][ydic[yl]-1]-ru[xdic[xl]-1][ydic[yr]]+ru[xdic[xl]-1][ydic[yl]-1] >=k:
            ans=min(ans,(xr-xl)*(yr-yl))
print(ans)