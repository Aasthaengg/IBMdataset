#!/usr/bin/env python3
(n, k), *q = [[*map(int, i.split())] for i in open(0)]
bucket = [0] * (10**5 + 1)
for a, b in q:
    bucket[a] += b
for n, i in enumerate(bucket):
    k -= i
    if k <= 0:
        print(n)
        break
