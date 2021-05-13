#!/usr/bin/env python3
s = input()
n = len(s)
for i in range(1,n):
    m = n - i
    if m % 2 > 0:
        continue
    if s[:m//2] == s[m//2:m]:
        print(m)
        exit()
