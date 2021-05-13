#!/usr/bin/env python3
s = input()
ans = 0
a = s.count('1')
b = s.count('0')
if a == 0 or b == 0:
    print(0)
    quit()
print(min(a, b)*2)
