#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code

def resolve():
    a,b,c=pin()
    t=(c-(a-b))
    if t<0:t=0
    print(t)
#%%submit!
resolve()