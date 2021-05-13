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
    N,A,B=pin()
    tt=abs(A-B)
    if tt%2==0:
        print(tt//2)
        return
    else:
        s= max(A,B)-1
        t=N-min(A,B)
        print(min(s,t,(tt-1)//2+1)+min(min(A,B)-1,N-max(A,B)))
#%%submit!
resolve()