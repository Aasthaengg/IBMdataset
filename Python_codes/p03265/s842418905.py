#print#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
def lispin(t=int):return list(pin(t))
#%%code
from fractions import gcd
def resolve():
    x1,y1,x2,y2=pin()
    a=y2-y1
    b=x2-x1
    x3=x2-a;y3=y2+b
    x4=x1-a;y4=y1+b
    print(x3,y3,x4,y4)
    
        
#%%submit!    
resolve()