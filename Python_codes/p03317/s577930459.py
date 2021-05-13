# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:56:28 2020

@author: liang
"""
from math import ceil

N, K = map(int, input().split())
A = [int(x) for x in input().split()]
ans = ceil((N-K)/(K-1)) + 1
print(ans) 