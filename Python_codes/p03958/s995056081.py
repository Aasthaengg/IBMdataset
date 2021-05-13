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

k,t=map(int,input().split())
a=list(map(int,input().split()))

lst=[]
for i in range(t):
    lst.append([-a[i],i])
heapq.heapify(lst)

mae=[0,-1]
while lst:
    now,id=heapq.heappop(lst)
    now+=1
    if mae[0]!=0:
        heapq.heappush(lst,mae)
    mae=[now,id]
print(-mae[0])