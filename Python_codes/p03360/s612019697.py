# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:23:47 2020

@author: shinba
"""

A = list(map(int,input().split()))
k = int(input())

A.sort()

print(A[2]*(2**k)+A[0]+A[1])

