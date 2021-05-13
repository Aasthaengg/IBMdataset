# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:30:59 2020

@author: shinba
"""

a,b = map(str,input().split())

if a == "H":
    if b == "H":
        print("H")
    else:
        print("D")
else:
    if b == "H":
        print("D")
    else:
        print("H")
    
