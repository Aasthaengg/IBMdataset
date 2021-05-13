# -*- coding: utf-8 -*-

def infinite_product(n, k):
    inpr = 1
    if k == 0:
        k = 1
    
    for i in range(n, k+1):
        inpr *= i
    
    return inpr


s = input().split()
N = int(s[0])
K = int(s[1])

print(N-K+1)