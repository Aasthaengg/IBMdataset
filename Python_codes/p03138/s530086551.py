import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=10**9+7

n,k=map(int,input().split())
a=list(map(int,input().split()))
m=0
if k==0:
    m=int(math.log2(1)+1)
else:
    m=int(math.log2(k)+1)
lst=[0]*m
for i in range(n):
    for j in range(m):
        if a[i]&(1<<j):
            lst[j]+=1
# print(lst)

ans=0
ans2=0
for i in range(m):
    if lst[m-i-1]<=n/2 and ans+pow(2,m-i-1)<=k:
        ans+=pow(2,m-i-1)
# print(ans)
# print(ans2)
for i in range(n):
    ans2+=ans^a[i]

print(ans2)
