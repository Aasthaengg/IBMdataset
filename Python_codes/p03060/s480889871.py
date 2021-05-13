n,a=int(input()),0
V=list(map(int,input().split()))
C=list(map(int,input().split()))
ans=[0 for _ in range(n)]

for i in range(n):
  ans = V[i] - C[i]
  if ans > 0:
    a += ans
  
print(a)