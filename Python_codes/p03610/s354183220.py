# -*- coding: utf-8 -*-

s = list(input())

output=""
for i,ss in enumerate(s):
    if i % 2 == 0:
        output += ss

print(output)
