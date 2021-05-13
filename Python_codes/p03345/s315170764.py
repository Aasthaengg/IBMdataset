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
    A,B,C,K=pin()
    
    k=K%2
    t=(A-B)
    if abs(t)>10**18:print("Unfair");return
    if k%2:t=(-1)*t
    print(t)
    #print(A,B,C)


#%%submit!
resolve()
