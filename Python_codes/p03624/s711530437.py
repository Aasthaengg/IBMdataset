#!/usr/bin/env python3
a = [0] * 26
s = input()
for i in s:
    a[ord(i) - 97] = 1
print('None'*(sum(a)==26) or chr(a.index(0) + 97))
