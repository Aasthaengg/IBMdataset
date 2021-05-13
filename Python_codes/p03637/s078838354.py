# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:11:12 2020

@author: shinba
"""

n = int(input())

a = map(int,input().split())

two = 0
four = 0

b = []

for i in a:
    if i % 2 == 0:
        b.append(i//2)

for i in b:
    if i % 2 == 0:
        four += 1
    else:
        two += 1

if two == 0:
    if n <= 2*four +1:
        print("Yes")
    else:
        print("No")
else:
    if n - two <= 2*four:
        print("Yes")
    else:
        print("No")