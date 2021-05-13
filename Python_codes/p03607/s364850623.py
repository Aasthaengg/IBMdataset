#!/usr/bin/env python3
n = int(input())
a = [int(input()) for i in range(n)]
d = {}

for i in a:
    if i in d:
        del d[i]
    else:
        d[i] = i

print(len(d))
