# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:51:17 2020

@author: liang
"""
A, B = map(int, input().split())

res = B*10

for i in range(10):
    tmp =int((res + i)*0.08)
    if  tmp == A:
        print(res+i)
        break
else:
    print(-1)