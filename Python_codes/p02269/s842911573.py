#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin
n = int(stdin.readline())
readline = stdin.readline
d = dict()
while n:
    n -= 1
    cmd, c = readline().split()
    if cmd.startswith('i'):
        d[c] = True
    elif d.get(c):
        print('yes')
    else:
        print('no')