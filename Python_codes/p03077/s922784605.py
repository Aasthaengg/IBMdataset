import bisect, copy, heapq, math
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

n=int(input())
abcde=[int(input()) for i in range(5)]
# print(n,abcde)

ans=4
for i in range(5):
    if min(abcde)==abcde[i]:
        ans+=math.ceil(n/abcde[i])
        break
print(ans)