#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
147 105

output:
21
"""

import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    n1, n2 = map(int, _input[0].split())
    print(gcd(n1, n2))