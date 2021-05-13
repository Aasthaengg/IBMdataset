#!/usr/bin/env python3
n, k, q, *a = map(int, open(0).read().split())
r = [k - q] * n
for i in a:
    r[i - 1] += 1
for i in r:
    if i > 0:
        print("Yes")
    else:
        print("No")
