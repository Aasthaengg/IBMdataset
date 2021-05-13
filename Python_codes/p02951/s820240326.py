# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:48:45 2020

@author: Kanaru Sato
"""

a,b,c = list(map(int,input().split()))

ans = c-a+b
if ans <= 0:
    print(0)
else:
    print(ans)