# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:25:07 2020

@author: NEC-PCuser
"""

N, K = map(int, input().split())

A = list(map(int, input().split()))

tentosu = 0

MOD = 1000000007

for i in range(0, N):
    a = 0
    d = 0
    """
    for j in range(0, N):
        if (i == j):
            continue
        if (i < j and A[i] > A[j]):
            a += 1
        if (A[i] > A[j]):
            d += 1
    """
    for j in range(0, N):
        if (A[i] > A[j]):
            d += 1
    for j in range(i, N):
        if (A[i] > A[j]):
            a += 1
    
    
    tentosu += a * K + (K - 1) * K * d // 2;
    
print(tentosu % MOD)