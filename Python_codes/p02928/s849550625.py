#!/usr/bin/env python3

#import
#import math
#import numpy as np
N, K = map(int, input().split())
A = list(map(int, input().split()))

t1 = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            t1 += 1

A.sort()
t2 = 0
lst = 0
for i in range(1, N):
    if A[i - 1] < A[i]:
        t2 += i
        lst = i
    elif A[i - 1] == A[i]:
        t2 += lst

ans = (t1 * K + t2 * K * (K - 1) // 2) % (10 ** 9 + 7)

print(ans)


