import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7

n,u,v=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n-1)]

dic=defaultdict(list)
for i in range(n-1):
    a,b=ab[i]
    dic[a].append(b)
    dic[b].append(a)
# print(dic)

taka=[-1]*(n+1)
aoki=[-1]*(n+1)

d=deque([[u,0]])
if len(dic[u])==1:
    taka[u]=0
while d:
    now,cnt=d.popleft()
    flag=0
    for i in range(len(dic[now])):
        if taka[dic[now][i]]==-1:
            taka[dic[now][i]]=-2
            flag=1
            d.append([dic[now][i],cnt+1])
    if flag==0:
        taka[now]=cnt
# print(taka)

d=deque([[v,0]])
if len(dic[v])==1:
    aoki[v]=0
while d:
    now,cnt=d.popleft()
    flag=0
    for i in range(len(dic[now])):
        if aoki[dic[now][i]]==-1:
            aoki[dic[now][i]]=-2
            flag=1
            d.append([dic[now][i],cnt+1])
    if flag==0:
        aoki[now]=cnt
# print(aoki)

ans=0
for i in range(n+1):
    if taka[i]<aoki[i]:
        ans=max(ans, aoki[i]-1)
print(ans)