# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:07:38 2020

@author: Kanaru Sato
"""

a,b = list(map(int, input().split()))

if a >= 10 or b >= 10:
    print("-1")
else:
    print(a*b)