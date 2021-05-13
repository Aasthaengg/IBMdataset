# -*- coding: utf-8 -*-
"""
D - Water Bottle
https://atcoder.jp/contests/abc144/tasks/abc144_d

"""
import sys


from math import tan, radians, pi

def is_ok(a, b, x, d):
    if b * tan(pi/2 - radians(d)) <= a:
        return (b * b * tan(pi/2 - radians(d)) * a) / 2 >= x
    else:
        return a * a * (b - a * tan(radians(d))) + (a * a * a * tan(radians(d))) / 2 >= x


def solve(a, b, x):
    lb, ub = 0.0, 90.0
    for _ in range(100):
        mid = (lb + ub) / 2
        if is_ok(a, b, x, mid):
            lb = mid
        else:
            ub = mid
    return (lb + ub) / 2


def main(args):
    a, b, x = map(int, input().split())
    ans = solve(a, b, x)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
