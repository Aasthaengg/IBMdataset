# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = map(int, raw_input().split())

a = n[0]
b = n[1]
c = n[2]

if(a < b and b < c):
    print "Yes"
else:
    print "No"