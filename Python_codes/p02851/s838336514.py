#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,K=map(int,input().split())
A = list(map(int,input().split()))
for i in range(n):
    A[i]-=1
B=[0]+A[:]
for i in range(n):
    B[i+1]=(B[i+1]+B[i])%K
C=collections.Counter(B[:K])
for ci in C.values():
    ans+=ci*(ci-1)//2
for i in range(K,n+1):
    # print(ans)
    C[B[i-K]]-=1
    ans+=C[B[i]]
    C[B[i]]+=1
# print(B)
# print(C)
print(ans)
