# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 02:46:31 2020

@author: liang
"""

N = int(input())
P = [int(x) for x in input().split()]

low = P[0]
count = 0

for p in P:
    if low >= p:
        low = p
        count += 1
print(count)