# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:30:35 2020

@author: shinba
"""

s = input()

a = s.count("a")
b = s.count("b")
c = s.count("c")

L = [a,b,c]

L.sort()

if L[2]-L[0] <= 1:
    print("YES")
else:
    print("NO")