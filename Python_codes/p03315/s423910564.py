#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    cnt=0
    for i in input():
        if i =="-":
            cnt-=1
        else:cnt+=1
    print(cnt)
        
#%%submit!
resolve()
