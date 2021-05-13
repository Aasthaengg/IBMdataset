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
    N,=pin()
    A=lispin()
    A.sort()
    #print(A)
    temp=0
    for i in range(N*2):
        t=A.pop()
        if i%2:temp+=t
    print(temp)
#%%submit!
resolve()