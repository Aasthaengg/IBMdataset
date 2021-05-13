# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:42:47 2020

@author: shinba
"""

a,b = map(int,input().split())

if a+b < 24:
    print(a+b)
else:
    print(a+b-24)