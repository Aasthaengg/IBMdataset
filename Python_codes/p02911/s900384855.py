#!/usr/bin/env python3

N,K,Q = [int(i) for i in input().split()]
A = [0]*(Q+1)
P = [K-Q]*(N+1)
for i in range(1,Q+1):
    A[i] = int(input())
    P[A[i]] += 1

for p in P[1:]:
    if p <= 0:
        print("No")
    else:
        print("Yes")
