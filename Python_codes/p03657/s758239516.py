# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:29:30 2020

@author: shinba
"""

a,b = map(int,input().split())

if a % 3 == 0:
    print("Possible")
elif b % 3 == 0:
    print("Possible")
elif (a+b) % 3 == 0:
    print("Possible")
else:
    print("Impossible")
