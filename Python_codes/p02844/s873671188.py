#!/usr/bin/env python3
n = int(input())
s = input()
c = 0
for i in range(10):
    a = s.find(str(i))
    if a > -1:
        for j in range(10):
            b = s.find(str(j), a + 1)
            if b > -1:
                c += len(set(s[b + 1:]))
print(c)
