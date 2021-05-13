#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    N, A, B = read_h()

    if A % 2 == B % 2:
        print('Alice')
    else:
        print('Borys')


if __name__ == '__main__':
    main()
