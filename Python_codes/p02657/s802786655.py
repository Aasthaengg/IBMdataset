#!/usr/bin/env python
# coding: utf-8

import sys


def main():
    line = sys.stdin.readline()
    t = line.rstrip().split(' ')
    a, b = map(lambda x: int(x), t)
    print(a*b)

    for line in sys.stdin:
        print(line)


if __name__ == '__main__':
    main()