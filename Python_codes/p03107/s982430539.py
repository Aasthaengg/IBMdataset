#!/usr/bin/env python3
s = input()
n = len(s)
c = 0
p = ""
count = 0
for i in s:
    if i == p:
        count += 1
    else:
        c = count - c
        count = 1
    p = i
c = count - c
print(n - abs(c))
