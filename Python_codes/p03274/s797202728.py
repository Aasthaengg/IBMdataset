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

n,k=map(int,input().split())
x=list(map(int,input().split()))

rui=[0]
for i in range(n-1):
    rui.append(x[i+1]-x[i]+rui[i])
# print(rui)

ans=float('inf')
for i in range(n-k+1):
    tmp=rui[i+k-1]-rui[i]
    ans=min(ans,tmp+min(abs(x[i]),abs(x[i+k-1])))
print(ans)