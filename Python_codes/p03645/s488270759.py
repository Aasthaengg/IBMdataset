#!/usr/bin/env python3
n, m = input().split()
a = set()
b = set()
for _ in range(int(m)):
    r = set(input().split())
    if "1" in r:
        a |= r
    if n in r:
        b |= r
print("POSSIBLE" if len(a & b) > 0 else "IMPOSSIBLE")
