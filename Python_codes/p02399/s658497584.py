# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 11:58:46 2015

@author: hirose
"""

n = map(int, raw_input().split())

a = n[0]
b = n[1]

#print a/b, a%b, float(a)/b
print '%d %d %f' %(a/b, a%b, float(a)/b)