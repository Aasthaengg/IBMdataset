#!/usr/bin/env python3
n, *b = map(int, open(0).read().split())
l = []
while True:
    F = 1
    for i, j in enumerate(b[::-1]):
        if len(b) - i == j:
            del b[len(b) - i - 1]
            l += j,
            F = 0
            break
    if F:
        break
if b:
    exit(print(-1))
for i in l[::-1]:
    print(i)