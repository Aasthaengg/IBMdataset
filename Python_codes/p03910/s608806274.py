#!/usr/bin/env python3
#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):return map(type,input().split())
def tupin(t=int):return tuple(pin(t))
#%%code
def resolve():
    N,=pin()
    temp=0
    ans=[]
    dame=0
    end=0
    for i in range(1,10**7):
        temp+=i
        if temp>=N:
            dame=temp-N
            end=i
            break
    for j in range(1,end+1):
        if j!=dame:print(j)
#%%submit!
resolve()