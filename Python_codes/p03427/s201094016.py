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
    N=list(input())
    a=sum(map(int,N))
    for n in range(1,len(N)):
        t=(N[:n]+[9]*(len(N)-n))
        a=max(a,sum(map(int,t))-1)
    print(a)
        
#%%submit!
resolve()