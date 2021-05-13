# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 16:38:31 2015

@author: hirose
"""

#Branch on Condition - Sorting Three Numbers

n = map(int, raw_input().split())

a = n[0]
b = n[1]
c = n[2]

for i in range(3):
    for i in range(2):
        if(n[i] > n[i+1]):
            temp = n[i]
            n[i] = n[i+1]
            n[i+1] = temp

print n[0], n[1], n[2]