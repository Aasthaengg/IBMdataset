#!/usr/bin/env python3
s = input()
a = s.count("a")
b = s.count("b")
c = s.count("c")
if abs(a - b) < 2 and abs(a - c) < 2 and abs(c - b) < 2:
    print("YES")
else:
    print("NO")
