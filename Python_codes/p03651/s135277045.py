#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
from fractions import gcd
from functools import reduce
def resolve():
    N,K=pin()
    A=list(pin())
    A.sort()
    maxK=A[-1]
    step=reduce(gcd,A)
    cond=1
    if K>maxK or (maxK-K)%step!=0:cond=0
    print(["IMPOSSIBLE","POSSIBLE"][cond])

#%%submit!
resolve()