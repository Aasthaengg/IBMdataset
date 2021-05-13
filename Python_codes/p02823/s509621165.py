# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:22:34 2020

@author: shinba
"""
import sys 
n,a,b = map(int,input().split())

if (b-a) % 2 == 0:
    print((b-a)//2)
    sys.exit()
    
k = (a+b-1)//2

print(min(k,n-k))

