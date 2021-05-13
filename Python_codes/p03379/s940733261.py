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
x=list(map(int,input().split()))
tmp=sorted(x)

if n%2==0:
    heikin=(tmp[n//2]+tmp[n//2-1])/2
    for i in range(n):
        if heikin<x[i]:
            print(tmp[n//2-1])
        else:
            print(tmp[n//2])

