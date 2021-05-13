# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 12:20:19 2015

@author: hirose
"""
import math

n = map(float, raw_input().split())

r = n[0]

print '%f %f' %(math.pi*r*r, 2*math.pi*r)

exit(0)