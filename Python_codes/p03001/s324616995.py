# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:13:44 2020

@author: shinba
"""
import sys

w,h,x,y = map(int,input().split())

if w%2 == 0 and h%2 == 0:
    if w//2 == x and h//2 == y:
        print((h*w)/2,1)
        sys.exit()
        
print(h*w/2,0)