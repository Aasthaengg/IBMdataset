#!/usr/bin/env python3
s = input()
o = [i == "L" for i in s[::2]] + [i == "R" for i in s[1::2]]
print("YNeos"[sum(o) != 0::2])
