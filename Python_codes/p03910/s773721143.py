# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 20:20:11 2020

@author: NEC-PCuser
"""


N = int(input())

i = 1
li = []
while (N >= (i * (i + 1)) // 2):
    li.append(i)
    i += 1
    

value = (i - 1) * i // 2

index = len(li) - 1
for i in range(value, N):
    li[index] += 1
    index -= 1

for i in li:
    print(i)