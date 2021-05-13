# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:04:30 2020

@author: liang
"""

N, M = map(int,input().split())

if N == 1 and M == 1:
    ans = 1
elif N == 1:
    ans = M - 2
elif M == 1:
    ans = N - 2
else:
    ans = (N-2)*(M-2)
print(ans)