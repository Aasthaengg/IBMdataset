# -*- coding: utf-8 -*-
"""
Created on Tue May 12 01:19:32 2020

@author: shinba
"""
import collections

n = int(input())

A = list(map(int,input().split()))

data = collections.Counter(A)

I = sorted(data.items(),reverse = True)
#print(I)
s1 = 0
s2 = 1
cnt1 = 0
cnt2 = 0 

for i,j in I:
    if cnt1 == 0 and j >= 4:
        s1 = i**2
        cnt1 = 1
    if j >= 2:
        s2 *= i
        cnt2 += 1
    if cnt2 == 2:
        print(max(s1,s2))
        break
else:
    if s1 != 0:
        print(s1)
    else:
        print(0)