#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    A = list(map(int, input().split()))

    odd = sum(a % 2 for a in A)
    four = sum(a % 4 == 0 for a in A)
    even = N - odd

    if even - four:
        if four >= odd:
            print('Yes')
        else:
            print('No')
    else:
        if four >= odd - 1:
            print('Yes')
        else:
            print('No')


if __name__ == "__main__":
    main()
