# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 11:29:17 2015

@author: hirose
"""

n = map(int, raw_input().split())

a = n[0]
b = n[1]
c = n[2]

x = a
number = 0

while(1):
    if(c % x == 0):
        number += 1
    x += 1
    if(x > b):
        break
print number
exit(0)