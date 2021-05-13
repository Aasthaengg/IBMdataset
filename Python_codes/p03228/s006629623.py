# -*- coding: utf-8 -*-

import sys

line = sys.stdin.readline()
A, B, K = ( int(s) for s in line.split() )

x, y = A, B

for _ in range(K):
    #if x % 2 == 1:
    #    x -= 1
    x -= x % 2
    n = x // 2
    x -= n
    y += n
    x, y = y, x

if K % 2 == 1:
    x, y = y, x

print("%s %s" % (x, y))
