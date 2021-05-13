# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:18:03 2020

@author: liang
"""
N, K, Q = map(int, input().split())
A = [0]*N
for i in range(Q):
    t = int(input())
    A[t-1] += 1

#print(A)
for i in range(N):
   # print(Q-A[i])
    if Q - A[i] <  K:
        print("Yes")
    else:
        print("No")