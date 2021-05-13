# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:27:39 2020

@author: shinba
"""

x = int(input())

if x%11 == 0:
    print(2*(x//11))
elif x%11 <=6:
    print(2*(x//11)+1)
else:
    print(2*(x//11)+2)
