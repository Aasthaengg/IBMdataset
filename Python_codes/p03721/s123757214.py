# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 01:14:47 2020

@author: liang
"""

N, K = map(int,input().split())
A = list()
for i in range(N):
    a, b = map(int,input().split())
    A.append((a,b))
A.sort(key= lambda x:x[0])

tmp = 0
for i in range(N):
    a, b = A[i]
    tmp += b
    if tmp >= K:
        print(a)
        break
