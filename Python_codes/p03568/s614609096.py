#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
def resolve():
    N=int(input())
    t=3**N
    s=1
    f=0
    for a in pin():
        if  a%2:
            f=1
            s*=1
        else:
            s*=2

    print(t-s)
#%%submit!
resolve()