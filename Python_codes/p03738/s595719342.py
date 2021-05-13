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
    A=int(input())
    B=int(input())
    if A==B:print("EQUAL")
    else:print(["LESS","GREATER"][A>B])

#%%submit!
resolve()


