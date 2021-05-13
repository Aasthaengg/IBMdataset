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
    N,=pin()
    A=lispin()
    temp=A[0]
    for i in range(1,N):
        temp=(temp*A[i])//(gcd(temp,A[i]))
    x=(temp-1)
    ans=0
    for a in A:
        ans+=x%a
    print(ans)
#%%submit!
resolve()