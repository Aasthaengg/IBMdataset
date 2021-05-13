# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:00:04 2020
"""

import sys
#import numpy as np

sys.setrecursionlimit(10 ** 9)
#def input():
#    return sys.stdin.readline()[:-1]
mod = 10**9+7

#N = int(input())
N,A,B = map(int,input().split())
#A = list(map(int,input().split()))


b = A + B - N if A + B - N >=0 else 0
ans = [str(min(A,B)),str(b)]

print(' '.join(ans))
