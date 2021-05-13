#!/usr/bin/env python3
N = int(input())

def query(x):
    print(x, flush=True)
    res = input()
    if res == 'Vacant':
        exit()
    return res

l, r = 0, N - 1
ql = query(l)
qr = query(r)
while True:
    m = (l + r) // 2
    qm = query(m)
    if (qm == ql) == (m % 2 == l % 2):
        l = m
        ql = qm
    else:
        r = m
