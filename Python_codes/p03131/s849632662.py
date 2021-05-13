#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    K,A,B=pin()
    t=(B-A)/2
    if K<A or B-A<=2:
        print(K+1)
        return
    K-=(A-1)
    cnt=A
    p,q=K%2,K//2
    cnt+=(B-A)*q+p
    print(cnt)

#%%submit!
resolve()
