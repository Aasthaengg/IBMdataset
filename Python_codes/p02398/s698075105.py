# -*- coding: utf-8 -*-

import sys

cnt = 0
for line in sys.stdin.readlines():
    a, b, c = map(int, line.strip().split())
    for x in range(a, b+1):
        if c % x == 0:
            cnt += 1

print(cnt)