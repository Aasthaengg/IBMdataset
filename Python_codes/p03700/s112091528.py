#!/usr/bin/env python3
import sys
from math import ceil
input = lambda: sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**8)
inf = float('inf')
mod = 10**9+7

n,a,b=map(int,input().split())
h=[]
for i in range(n):
    h.append(int(input()))
ok=inf
left=1
right=10**9+10
while left<right:
    mid=(left+right)//2
    tmp=0
    for hi in h:
        tmp+=max(0,ceil((hi-mid*b)/(a-b)))
    if tmp>mid:
        left = mid+1
    else:
        right=mid
        ok=min(ok,mid)
print(ok)


