# -*- coding:utf-8 -*-
from math import *
n = input()
xli=map(float,raw_input().split())
yli=map(float,raw_input().split())
md1 = 0 #minkowski distance p=1
md2 = 0 #p=2
md3 = 0 #p=3
mdinf = 0 #p=???(infinity)
for i in xrange(n):
    d = fabs(xli[i]-yli[i])
    md1 += d
    md2 += d**2
    md3 += d**3
    if d>mdinf:
        mdinf = d
md2 = md2**(1/2.0)
md3 = md3**(1/3.0)
print md1
print md2
print md3
print mdinf