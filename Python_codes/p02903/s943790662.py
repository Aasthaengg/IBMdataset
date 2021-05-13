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

h,w,a,b=map(int,input().split())

lst=[[""]*w for i in range(h)]
# print(lst)

l,r=0,a

for i in range(h):
    for j in range(w):
        if l<=j<r:
            if i<b:
                lst[i][j]="0"
            else:
                lst[i][j]="1"
        else:
            if i<b:
                lst[i][j]="1"
            else:
                lst[i][j]="0"

for i in range(h):
    print("".join(lst[i]))