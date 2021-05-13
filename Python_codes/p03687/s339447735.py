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

s=input()

cnter=Counter(s)

ans=float('inf')
for a in al:
    if cnter[a]==0:
        continue
    tmp=s[:]
    cnt=0
    while 1:
        flag=1
        for i in range(len(tmp)):
            if a!=tmp[i]:
                flag=0
        if flag==1:
            break
        tmp1=""
        for i in range(len(tmp)-1):
            if tmp[i]==a or tmp[i+1]==a:
                tmp1+=a
            else:
                tmp1+=tmp[i]
        cnt+=1
        tmp=tmp1[:]
    ans=min(ans,cnt)
print(ans)