import sys
#import numpy as np
import math
from fractions import Fraction
import itertools

input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
p=[0]*n
q=[0]*n
ans=0
mod=10**9+7
for i in range(n):
    for j in range(n):
        if a[i]>a[j]:
            if i>j:
                p[i]+=1
            elif i<j:
                q[i]+=1
                
for i in range(n):
    ans+=(k*q[i]+((p[i]+q[i])*k*(k-1)//2)%mod)%mod
    ans=ans%mod
print(int(ans%mod))