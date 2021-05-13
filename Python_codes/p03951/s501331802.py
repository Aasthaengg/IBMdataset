# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:43:29 2020

@author: shinba
"""

n = int(input())
s = input()
t = input()

l = 0
for i in range(n):
    if s[i:] == t[:n-i]: 
         l = n-i
         break

print(2*n-l)
    
