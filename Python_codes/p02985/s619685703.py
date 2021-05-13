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

n,k=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n-1)]

dic=defaultdict(list)
for i in range(n-1):
    a,b=ab[i]
    dic[a].append(b)
    dic[b].append(a)
# print(dic)

itta=[0]*(n+1)
itta[1]=1
d=deque([[1,0,0]])

ans=k
while d:
    tmp=d.popleft()
    now,one,two=tmp
    j=0
    for i in range(len(dic[now])):
        if itta[dic[now][i]]==0:
            itta[dic[now][i]]=1
            ans*=k-1-two-j
            j+=1
            d.append([dic[now][i],one,one+1])
            ans%=mod
    # print(tmp,ans)

print(ans)