#! /usr/bin/env python3

import sys
import numpy as np
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)


def query(q):
    print(q, flush=True)
    s = readline().decode().rstrip()
    if s[0] == 'V':
        sys.exit()
    return s


N = int(readline())

s = query(0)
l = 0
r = N
sex = s

while True:
    m = (l + r) // 2
    s = query(m)
    if sex == s:
        if (m - l) % 2:
            r = m
        else:
            l = m
    else:
        if (m - l) % 2:
            l = m
            sex = s
        else:
            r = m