# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:16:23 2020

@author: shinba
"""

s = input()

start = s[0]
cnt1 = 0

for i in range(1,len(s)):
    if s[i] == start:
        continue
    cnt1 += 1
    start = s[i]

start = s[-1]
cnt2 = 0

for i in range(len(s)-1,-1,-1):
    if s[i] == start:
        continue
    cnt2 += 1
    start = s[i]

print(min(cnt1,cnt2))