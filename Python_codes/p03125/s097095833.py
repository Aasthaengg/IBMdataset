# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:55:48 2020
"""

import sys
#import numpy as np

sys.setrecursionlimit(10 ** 9)
#def input():
#    return sys.stdin.readline()[:-1]
mod = 10**9+7

#N = int(input())
A, B = map(int,input().split())

if B % A == 0:
    print(A+B)
else:
    print(B-A)

