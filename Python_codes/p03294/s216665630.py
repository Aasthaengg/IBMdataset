# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:46:20 2020

@author: shinba
"""

n = int(input())

ans = 0

for i in map(int,input().split()):
    ans += i

print(ans-n)


