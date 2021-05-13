import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

h,w=map(int,input().split())
a=[input() for i in range(h)]

itta=[[0]*w for i in range(h)]
itta[0][0]=1
d=deque([[0,0]])
while d:
    nh,nw=d.popleft()
    itta[nh][nw]%=mod
    if nh+1<h and a[nh+1][nw]==".":
        if itta[nh+1][nw]==0:
            d.append([nh+1,nw])
        itta[nh+1][nw]+=itta[nh][nw]
    if nw+1<w and a[nh][nw+1]==".":
        if itta[nh][nw+1]==0:
            d.append([nh,nw+1])
        itta[nh][nw+1]+=itta[nh][nw]

print(itta[-1][-1]%mod)