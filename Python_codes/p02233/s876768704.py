#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


# def fib_bad(n):
#     if not n or n == 1:
#         return 1
#     return fib_bad(n - 2) + fib_bad(n - 1)


def fib_dp(n):
    fib_list[:1] = [1, 1]
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 2] + fib_list[i - 1]
    return fib_list.pop()


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    index = int(_input[0])
    fib_list = [None] * index
    print(fib_dp(index))