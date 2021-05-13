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

n=int(input())
xy=[list(map(int,input().split())) for i in range(n)]

# dic={}
# for i in range(n):
#     x,y=xy[i]
#     dic[(x,y)]=1
if n==1:
    print(1)
    quit()
cnt=0
sadic=defaultdict(int)
for i in range(n):
    x,y=xy[i]
    for j in range(n):
        if i==j:
            continue
        x2,y2=xy[j]
        p,q=x-x2,y-y2
        sadic[(p,q)]+=1
# print(sadic)
print(n-max(sadic.values()))