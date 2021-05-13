# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:28:28 2020

@author: shinba
"""

n = int(input())

A = []
B = []

for i in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    
ans = 0

for i in range(n-1,-1,-1):
    sup = (A[i]+ans) % B[i]
    ans += B[i] - sup if sup != 0 else 0

print(ans)
    
    
    
    
