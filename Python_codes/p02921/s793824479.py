# -*- coding: utf-8 -*-

s = str(input())
t = str(input())

counter = 0

for i in range(len(s)):
    if s[i] == t[i]:
        counter = counter + 1

print(counter)