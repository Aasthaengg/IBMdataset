#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from collections import Counter
def resolve():
    A,B,K=pin()
    s=set()
    for i in range(K):
        if A+i<=B:s.add(A+i)
    
    for k in range(K):
        if (B+k-K+1)>=A: s.add(B+k-K+1)
    print(*sorted(list(s)),sep='\n')
    #print()
#%%submit!
resolve()