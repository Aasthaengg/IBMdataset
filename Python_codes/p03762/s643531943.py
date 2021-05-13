# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:35:12 2018

@author: maezawa
"""

n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ax = 0
for i in range(1,n):
    ax += (n-i)*i*(x[i]-x[i-1])%(10**9+7)

ay = 0
for j in range(1,m):
    ay += (m-j)*j*(y[j]-y[j-1])%(10**9+7)
    
print(ax*ay%(10**9+7))