# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:43:47 2020

@author: liang
"""

X, Y = map(int, input().split())

tmp = X
ans = 1

while tmp*2 <= Y:
    tmp *= 2
    ans += 1
    
print(ans)