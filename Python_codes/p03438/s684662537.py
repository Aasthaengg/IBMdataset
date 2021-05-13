# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:14:35 2020
"""

import sys
import numpy as np

sys.setrecursionlimit(10 ** 9)
#def input():
#    return sys.stdin.readline()[:-1]
mod = 10**9+7

N = int(input())
#X, Y = map(int,input().split())
a = np.array(list(map(int,input().split())))
b = np.array(list(map(int,input().split())))

c = b - a

ok = np.sum(c[c > 0]//2)
ng = np.sum(-c[c < 0])

if ok >= ng:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)