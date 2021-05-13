# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 21:20:10 2020

@author: NEC-PCuser
"""

N = (int(input()))

A = list(map(int, input().split()))

A.sort()

ans = 0
for i in range(0, len(A) - 1):
    if A[i] * 2 >= A[i + 1]:
        ans += 1
    else:
        ans = 0
    A[i + 1] += A[i]
        
ans += 1

print(ans)        