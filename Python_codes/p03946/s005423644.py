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
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,t=map(int,input().split())
a=list(map(int,input().split()))
lst=[0]*(n+1)

for i in range(n):
    lst[-2-i]=max(lst[-1-i],a[-1-i])
# print(lst)

sa=0
cnt=0
for i in range(n):
    if sa<lst[i]-a[i]:
        sa=lst[i]-a[i]
        cnt=1
    elif sa==lst[i]-a[i]:
        cnt+=1
    else:
        pass
print(cnt)