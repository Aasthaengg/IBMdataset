#!/usr/bin/env python3
n, *a = map(int, open(0).read().split())
b = [1] * n
i = 0
c = 0
while True:
    if b[i] < 1:
        break
    if i == 1:
        print(c)
        exit()
    b[i] = 0
    i = a[i] - 1
    c += 1
print(-1)
