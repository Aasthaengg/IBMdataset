# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:36:51 2020

@author: shinba
"""

n = list(input())

if (n[0] == n[1] and n[1] == n[2]) or (n[1] == n[2] and n[2] == n[3]):
    print("Yes")
else:
    print("No")