#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N,x=pin()
    A=list(pin())

    temp=A[0]
    ans=0
    if temp>x:
        A[0]=x
        ans+=temp-x
    
    for ai in range(1,N):
        temp=A[ai]+A[ai-1]
        if temp>x:
            A[ai]=x-A[ai-1]
            ans+=temp-x
        temp-=A[ai-1]
    print(ans)
        
#%%submit!
resolve()