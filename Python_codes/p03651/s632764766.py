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

n,k=map(int,input().split())
a=list(map(int,input().split()))

I="IMPOSSIBLE"
P="POSSIBLE"

if max(a)<k:
    print(I)
    quit()

gcd=a[0]
for i in range(n):
    gcd=math.gcd(gcd,a[i])

if k%gcd==0:
    print(P)
else:
    print(I)