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

a,b=map(int,input().split())
ans=0
for i in range(a,b+1):
    s=str(i)
    for j in range(len(s)//2):
        if s[j]!=s[-1-j]:
            break
    else:
        ans+=1
print(ans)