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
a=list(map(int,input().split()))
a.sort()
rui=list(accumulate(a))
# print(rui)

cnt=0
now=0
for now in range(n-1):
    if rui[now]*3>=rui[now+1]:
        cnt+=1
    else:
        cnt=0
print(cnt+1)