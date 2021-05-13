# -*- coding: utf-8 -*-
"""
Created on Fri May 15 00:22:18 2020

@author: Kanaru Sato
"""

n = int(input())
a = list(map(int,input().split()))

mot = 0.0
for i in range(n):
    mot += 1/a[i]
print(1/mot)