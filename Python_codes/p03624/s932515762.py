#!/usr/bin/env python3
arr = [chr(i) for i in range(97, 97+26)]
s = set([c for c in input()])

for c in arr:
    if not (c in s):
        print(c)
        break
else:
    print("None")
