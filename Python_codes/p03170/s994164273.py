import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
from functools import lru_cache
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,k=map(int,input().split())
a=list(map(int,input().split()))

lst=[0]*(k+1)
# for i in range(a[0]):
#     lst[i]=0
# print(lst)
# for i in range(a[0],a[-1]+1):
#     lst[i]=1
# print(lst)

for i in range(k+1):
    flag=1
    for j in range(n):
        if i-a[j]>=0:
            flag=min(flag,lst[i-a[j]])

    if flag==0:
        lst[i]=1
    else:
        lst[i]=0
# print(lst)
if lst[k]==1:
    print("First")
else:
    print("Second")