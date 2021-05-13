# -*- coding: utf-8 -*-

n = int(input())
s = str(input())
new = []

ntr = n % 26

for p in range(len(s)):
    k = ord(s[p]) + ntr
    if k > 90:
        k = k - 90 + 64
    new.append(chr(k))

x = "".join(new)
print(x)
