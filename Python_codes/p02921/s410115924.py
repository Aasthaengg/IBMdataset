# -*- coding: utf-8 -*-

s = str(input())
t = str(input())

counter = 0

counter = counter + 1 if s[0] == t[0] else counter
counter = counter + 1 if s[1] == t[1] else counter
counter = counter + 1 if s[2] == t[2] else counter

print(counter)