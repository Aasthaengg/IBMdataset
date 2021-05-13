import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

ans=0
for i in range(n):
    if x>=a[i]:
        x-=a[i]
        ans+=1
# print(x)
print(min(ans,n-1 if x>0 else n))