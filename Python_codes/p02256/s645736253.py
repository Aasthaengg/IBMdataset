#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
147 105

output:
21
"""

import sys


def gcd(x, y):
    if x < y:
        x, y = y, x

    while y > 0:
        r = x % y
        x = y
        y = r

    return x


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    n1, n2 = map(int, _input[0].split())
    print(gcd(n1, n2))