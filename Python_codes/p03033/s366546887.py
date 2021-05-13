import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,q=map(int,input().split())
stx=[list(map(int,input().split())) for i in range(n)]
d=[int(input()) for i in range(q)]

stx.sort(key=lambda x: x[2])

ans=[-1]*q
skip=[-1]*q

for i in range(n):
    s,t,x=stx[i]
    left=bisect.bisect_left(d, s-x)
    right=bisect.bisect_left(d, t-x)

    while left<right:
        if skip[left]==-1:
            ans[left]=x
            skip[left]=right
            left+=1

        else:
            left=skip[left]
    
print("\n".join(map(str,ans)))