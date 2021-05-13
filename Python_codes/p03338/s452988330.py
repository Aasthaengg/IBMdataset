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
s=input()
tmp=Counter(s)
ans=0
for i in range(n+1):
    l,r=s[:i],s[i:]
    dic={}
    tmp=Counter(r)
    for j in range(i):
        if tmp[l[j]]>0:
            dic[l[j]]=1
    ans=max(len(dic),ans)
    # print(l,r)
print(ans)