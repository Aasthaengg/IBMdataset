#!/usr/bin/python3
#coding: utf-8

import sys

N = int(input())

for h in range(1, 3501):
    for n in range(1, 3501):
        divisor = (4*h*n - N*h - N*n)
        if divisor <= 0:
            continue
        if (N*h*n) % divisor == 0:
            m = (N * h * n) // divisor
            print(h, n, m)
            sys.exit(0)
