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

n=int(input())
a=list(map(int,input().split()))

ans=0
flag=-1

for i in range(n-1):
    if flag==-1:
        if a[i]>a[i+1]:
            flag=0
        elif a[i]<a[i+1]:
            flag=1
    elif flag==1:
        if a[i]>a[i+1]:
            flag=-1
            ans+=1
    else:
        if a[i]<a[i+1]:
            flag=-1
            ans+=1

print(ans+1)