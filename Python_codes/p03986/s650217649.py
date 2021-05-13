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

x=input()

scnt=0
m=0
for i in range(len(x))[::-1]:
    if x[i]=="T":
        m=i+1
        break

ans=len(x)
for i in range(m):
    if x[i]=="S":
        scnt+=1
    else:
        if scnt>0:
            scnt-=1
            ans-=2
    # print(scnt)
print(ans)