import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    S = int(input())

    x1, y1 = 0, 0
    x2, y2 = 1000000000, 1
    y3 = math.ceil(S / 1000000000)
    x3 = x2 * y3 - S
    print('{} {} {} {} {} {}'.format(x1, y1, x2, y2, x3, y3))
