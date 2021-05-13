#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

L=input()
n=len(L)
dp1=[0]*(n+1); dp2=[0]*(n+1)
dp2[0]=1

for i in range(n):
    if L[i] == "1":
        dp1[i+1] = (dp1[i]*3 + dp2[i]) % mod
        dp2[i+1] = dp2[i]*2 % mod
    else:
        dp2[i+1] = dp2[i] % mod
        dp1[i+1] = dp1[i]*3 % mod
print((dp1[n] + dp2[n])%mod)