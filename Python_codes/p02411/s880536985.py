#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

while True:
    m, f, r = map(int, sys.stdin.readline().split())
    if m == -1 and f == -1 and r == -1:
        break
    elif m == -1 or f == -1:
        print('F')
    elif m+f >= 80:
        print('A')
    elif m+f >= 65:
        print('B')
    elif m+f >= 50:
        print('C')
    elif m+f >=30:
        if r >= 50:
            print('C')
        else:
            print('D')
    else:
        print('F')

