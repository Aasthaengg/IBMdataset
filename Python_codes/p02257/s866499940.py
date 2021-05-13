# -*- coding: utf-8 -*-

import math


def is_prime(x):
    # Primality Test
    if x == 2:
        return True

    if x <= 1 or x % 2 == 0:
        return False

    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2
    return True


def to_int(v):
    return int(v)


if __name__ == '__main__':
    l = to_int(input())
    seq = [to_int(input()) for i in range(l)]
    cnt = 0

    for v in seq:
        if is_prime(v):
            cnt += 1
    print(cnt)