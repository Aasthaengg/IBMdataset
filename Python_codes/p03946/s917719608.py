#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n,t = map(int,input().split())
A = list(map(int,input().split()))
B = [0] * n
acumin = A[0]
for i in range(n):
  acumin = min(acumin,A[i])
  B[i] = A[i] - acumin
C = collections.Counter(B)
print(C[max(B)])