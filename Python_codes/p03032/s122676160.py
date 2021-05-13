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
v=list(map(int,input().split()))

ans=0
for i in range(k+1):
    toru=i
    ireru=k-i
    # print(toru)
    for j in range(toru+1):
        l,r=j,n-(toru-j)
        if l>r:
            lst=v[:]
        else:
            lst=v[:l]+v[r:]
        # print(lst)
        lst.sort(reverse=True)
        for l in range(ireru):
            if lst and lst[-1]<0:
                lst.pop()
        ans=max(ans,sum(lst))

print(ans)