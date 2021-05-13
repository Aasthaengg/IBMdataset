# -*- coding: utf-8 -*-

s = list(str(input()))

a_start = 0
z_end = 0

# A の探索
for i in range(len(s)):
    if s[i] == 'A':
        a_start = i
        break

# Z の探索
for i in reversed(range(len(s))):
    if s[i] == 'Z':
        z_end = i
        break

print(len(s[a_start:z_end+1]))