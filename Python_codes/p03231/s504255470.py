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

n,m=map(int,input().split())
s=input()
t=input()
g=math.gcd(n,m)
for i in range(g):
    # print(s[n//g*i])
    if s[n//g*i]!=t[m//g*i]:
        print(-1)
        break
else:
    print(n*m//g)