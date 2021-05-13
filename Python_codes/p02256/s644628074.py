# -*- coding: utf-8 -*-


def gcd(x, y):
    # GCD(Greatest Common Divisor)
    if x < y:
        x, y = y, x

    while y > 0:
        r = x % y
        x = y
        y = r

    print(x)


def to_xy(v):
    return [int(c) for c in v.split()]


if __name__ == '__main__':
    x, y = to_xy(input())
    gcd(x, y)