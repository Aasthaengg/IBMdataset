#!/usr/bin/env python3

s = input()
d = [l1 == l2 for l1, l2 in zip(s, "CODEFESTIVAL2016")]
print(d.count(False))
