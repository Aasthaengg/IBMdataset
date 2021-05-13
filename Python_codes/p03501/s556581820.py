# -*- coding: utf-8 -*-
"""
Created on Thu May 14 01:20:03 2020

@author: shinba
"""

n,a,b = map(int,input().split())

if n*a >= b:
    print(b)
else:
    print(a*n)
