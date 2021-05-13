import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
mod=10**9+7

n,c=map(int,input().split())
stc=[list(map(int,input().split())) for i in range(n)]
stc.sort(key=lambda x: x[2])
# print(stc)
lst=[[0]*(10**5+5) for i in range(c)]
for i in range(len(stc)):
    s,t,c=stc[i]
    for j in range(s-1,t):
        lst[c-1][j]+=1
anslst=[0]*(10**5+5)
for i in range(c):
    for j in range(10**5+5):
        if lst[i][j]!=0:
            anslst[j]+=1
print(max(anslst))