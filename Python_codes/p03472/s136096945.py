#!/usr/bin/env python3
n, h, *A = map(int, open(0).read().split())
a = max(A[::2])
b = sorted(A[1::2])[::-1]
for i in range(n):
    if h <= 0:
        print(i)
        exit()
    if b[i] < a:
        print(i - (-h // a))
        exit()
    h -= b[i]
print(n - (-h // a))
