#!/usr/bin/env python
# -*- coding: utf-8 -*-

N, K = map(int, input().split())
A = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i):
        if A[i-j-1] > A[i-j]:
            tmp = A[i-j]
            A[i-j] = A[i-j-1]
            A[i-j-1] = tmp

for i in range(K):
    result += A[i]

print(result)

