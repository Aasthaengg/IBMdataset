# -*- coding: utf-8 -*-
"""
Created on Thu May 14 01:36:42 2020

@author: shinba
"""

n = int(input())
k = int(input())

a = 1
while n:
    a = min(a+k,a*2)
    n -= 1

print(a)
    
