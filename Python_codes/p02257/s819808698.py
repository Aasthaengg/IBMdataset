#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
input:
11
7
8
9
10
11
12
13
14
15
16
17

output:
4
"""

import sys
import math


def is_prime(x):
    if x == 2:
        return True
    elif x < 2 or not x % 2:
        return False

    i = 3
    x_sqrt = math.sqrt(x)
    while i <= x_sqrt:
        if not x % i:
            return False
        i += 2

    return True


def solve(_c_list):
    cnt = 0
    for ele in _c_list:
        if is_prime(ele):
            cnt += 1
    return cnt


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    c_num = int(_input[0])
    c_list = list(map(int, _input[1:]))
    ans = solve(c_list)
    print(ans)