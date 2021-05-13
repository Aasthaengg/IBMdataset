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
lst=[0]*n
for i in range(n-1):
    if h[i+1]<=h[i]:
        lst[i+1]=lst[i]+1
    else:
        lst[i+1]=0
# print(lst)
print(max(lst))