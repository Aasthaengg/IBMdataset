#!/usr/bin/env python3

c = input()
d = input()

if c == d[::-1] and d == c[::-1]:
    print("YES")
else:
    print("NO")