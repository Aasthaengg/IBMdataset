# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:22:31 2020

@author: liang
"""

N = int(input())
A = [int(x) for x in input().split()]

A.sort(reverse=True)

ans = list()
i = 0
while i < N-1:
    if A[i] == A[i+1]:
       # print("A")
        ans.append(A[i])
        i += 1
    if len(ans) == 2:
        break
    i += 1

import numpy as np
#print(ans)
if len(ans) < 2:
    print(0)
else:
    print(np.prod(ans))