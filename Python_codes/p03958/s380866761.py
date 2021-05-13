# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:25:46 2020

@author: NEC-PCuser
"""


K, T = map(int, input().split())

a = list(map(int, input().split()))

a.sort()

sum_cake = 0
for i in range(len(a) - 1):
   sum_cake += a[i]

if a[len(a) - 1] <= sum_cake + 1:
   print(0)
else:
    print(a[len(a) - 1]  - sum_cake - 1)