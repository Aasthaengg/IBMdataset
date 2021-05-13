#!/usr/bin/env python3
s = input()
f = s[0]
print("YNeos"[sum(f == i for i in s) != 2 or len({i for i in s}) != 2::2])
