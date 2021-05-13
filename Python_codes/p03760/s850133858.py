#!/usr/bin/env python3
o = input()
e = input() + "0"
s = ""
for a, b in zip(o, e[:len(o)]):
    s = s + a + b
print(s.replace("0", ""))
