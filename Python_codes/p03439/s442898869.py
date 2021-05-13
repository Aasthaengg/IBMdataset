#!/usr/bin/env python3
N = int(input())

print(0, flush=True)
w0 = input()
if w0 == 'Vacant':
    exit()

l, r = 0, N
while True:
    m = (l + r) // 2
    print(m, flush=True)
    w1 = input()
    if w1 == 'Vacant':
        break
    if m % 2 == (w0 != w1):
        l = m
    else:
        r = m
