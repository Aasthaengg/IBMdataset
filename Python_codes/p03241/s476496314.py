#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N,K=pin()
    t=K//N
    for i in range(t,0,-1):
        if K%i==0:
            print(i)
            return
        
#%%submit!
resolve()