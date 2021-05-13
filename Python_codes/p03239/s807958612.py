#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N,K=pin()
    c=[tupin() for i in range(N)]
    C=sorted(filter(lambda x:x[1]<=K,c))
    try:
        print(C[0][0])
    except :print("TLE")
#%%submit!
resolve()
