# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:32:18 2020

@author: NEC-PCuser
"""

a, b, x = map(int, input().split())

a_shou = a // x
b_shou = b // x

ans = b_shou - a_shou

if (a % x == 0):
    ans += 1

print(int(ans))