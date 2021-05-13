# -*- coding: utf-8 -*-

s = list(input())

g = 0
p = 0
for i in range(len(s)):
    if s[i] == "g":
        g += 1
    else:
        p += 1

ans = int((g-p) / 2)

print(ans)
