#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
a=list(map(int,input().split()))

Mod=10**9+7
M=10**6+2 #書き換え
fac=[0]*M
finv=[0]*M
inv=[0]*M

#finvに逆元、facに階乗のmod
def COMinit():
  fac[0]=fac[1]=1
  finv[0]=finv[1]=1
  inv[1]=1
  for i in range(2,M):
    fac[i]=(fac[i-1]*i%Mod)%Mod
    inv[i]=Mod-inv[Mod%i]*(Mod//i) %Mod
    finv[i]=(finv[i-1]*inv[i]%Mod)%Mod
def COM(n,k):
  if n<k:
    return 0
  if n<0 or k<0:
    return 0
  return (fac[n]*(finv[k]*finv[n-k]%Mod)%Mod)%Mod

COMinit()

def factorize(n):
    fct={}
    temp=n
    if temp<4:
        fct[temp]=1
    else:
        e=0
        while temp%2==0:
            temp=temp//2
            e+=1
        if e>0:
            fct[2]=e
    
    for b in range(3,int(n**0.5)+1,2):
        e=0
        while temp%b == 0:
            temp=temp//b
            e+=1
        if e>0:
            fct[b]=e
    if temp!=1:
        fct[temp]=1
    return fct

res={}
for i in a:
    f=factorize(i)
    for j in f:
        if j not in res:
            res[j]=f[j]
        else:
            res[j]=max(res[j],f[j])
c=1
ans=0
for i in res:
    c*=pow(i,res[i],Mod)
    c%=Mod
for i in a:
    ans+=c*inv[i]
    ans%=Mod
print(ans)
