# -*- coding: utf-8 -*-
"""
Created on Mon May  4 14:09:04 2020

@author: Kanaru Sato
"""

import sys
sys.setrecursionlimit(10**9)

n,m = list(map(int, input().split()))
thisconnected = [[] for i in range(n+1)]
thismemo = [-1 for i in range(n+1)]

for i in range(m):
    x,y = list(map(int, input().split()))
    thisconnected[x].append(y)

def lp(k,memo,connected):
    if memo[k] != -1:
        return memo[k]
    elif not connected[k]:
        memo[k] = 0
        return 0
    else:
        res = -1
        for point in connected[k]:
            if res < lp(point,memo,connected):
                res = lp(point,memo,connected)
        memo[k] = res+1
        return res+1

for i in range(1,n+1):
    if thismemo[i] == -1:
        thismemo[i] = lp(i,thismemo,thisconnected)

print(max(thismemo))