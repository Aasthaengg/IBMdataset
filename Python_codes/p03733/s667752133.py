#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N,T=pin()
    t=tupin()

    ans=0
    for i in range(1,N):
        temp=t[i]-t[i-1]
        if temp>T:ans+=T
        else: ans+=temp
    print(ans+T)
#%%submit!
resolve()