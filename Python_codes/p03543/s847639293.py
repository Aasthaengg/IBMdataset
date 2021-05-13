#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N=int(input())
    a=N//10
    b=N%1000
    print(["No","Yes"][a%111==0 or b%111==0])
    
#%%submit!
resolve()


