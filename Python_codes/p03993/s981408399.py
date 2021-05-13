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
    N,=pin()
    A=[i-1 for i in pin()]
    cnt=0
    for j in range(N):
        if A[A[j]]==j:cnt+=1
    print(cnt//2)
    
#%%submit!
resolve()
