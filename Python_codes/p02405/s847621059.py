# coding=utf-8
from __future__ import print_function


def gen(n, i=0):
    while n:
        yield '#' if i % 2 == 0 else '.'
        i += 1
        n -= 1


if __name__ == '__main__':
    while True:
        height, width = map(int, raw_input().split())
        if height + width == 0:
            break
        else:
            [print(''.join(list(gen(width, i)))) for i in xrange(height)]
            print()