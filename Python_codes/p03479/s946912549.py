#!/usr/bin/env python3

import sys

DEBUG = False

def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep = " "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    x, y = read_list(int)
    length = 0
    while x <= y:
        x *= 2
        length += 1
    print(length)


if __name__ == "__main__":
    main()