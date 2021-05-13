# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:11:18 2020

@author: Kanaru Sato
"""

n,k,c = list(map(int, input().split()))
s = list(input())

early = []
late = []

i = 0
count = 0
while i < n and count < k:
    if s[i] == "o":
        early.append(i)
        i = i+c+1
        count = count+1
    else:
        i = i+1


i = n-1
count = 0
while i > -1 and count < k:
    if s[i] == "o":
        late.append(i)
        i = i-c-1
        count = count+1
    else:
        i = i-1

for i in range(len(early)):
    if early[i] == late[k-i-1]:
        print(early[i]+1)