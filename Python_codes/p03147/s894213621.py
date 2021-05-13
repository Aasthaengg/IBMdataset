import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(500000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
h=list(map(int,input().split()))

ans=0
while sum(h)>0:
    flag=0
    for i in range(n):
        if flag==0:
            if h[i]>0:
                h[i]-=1
                flag=1
                ans+=1
            else:
                continue
        else:
            if h[i]>0:
                h[i]-=1
            else:
                flag=0
    # print(h)
print(ans)