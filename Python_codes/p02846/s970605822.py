#!/usr/bin/env python3
t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
d1 = (b1 - a1) * t1
d2 = (b2 - a2) * t2
if d1 > 0:
    d1 = -d1
    d2 = -d2
if d1 + d2 < 0:
    print(0)
    exit()
if d1 + d2 == 0:
    print('infinity')
    exit()

ok, ng = 0, 10**20
while ng - ok > 1:
    m = (ok + ng) // 2
    if m * d2 + (m + 1) * d1 <= 0:
        ok = m
    else:
        ng = m
if ok * d2 + (ok + 1) * d1 == 0:
    print(2 * ok)
else:
    print(2 * ok + 1)
