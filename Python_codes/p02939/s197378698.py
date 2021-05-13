#!/usr/bin/env python3
s = input()
c = [0] * len(s)
c[0] = 1
for i in range(1, len(s)):
    if i < 2:
        if s[i] == s[i - 1]:
            c[i] = c[i - 1]
        else:
            c[i] = c[i - 1] + 1
        continue
    if s[i] == s[i - 1]:
        c[i] = c[i - 3] + 2
    else:
        c[i] = c[i - 1] + 1
print(c[-1])
