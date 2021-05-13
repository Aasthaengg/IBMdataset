# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:22:58 2020

@author: shinba
"""

import bisect
x = int(input())
A = [n*(n+1)//2 for n in range(10**5)]

print(bisect.bisect_left(A,x))