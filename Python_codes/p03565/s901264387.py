#!/usr/bin/env python3
s = input()
t = input()
n = len(t)
m = len(s)
c = "z" * m
for i in range(m - n + 1):
    if all(j in (t[k], "?") for k, j in enumerate(s[i:n + i])):
        c = min(c, s[:i] + t + s[i + n:])
print("UNRESTORABLE" if c == "z" * m else c.replace("?", "a"))
