#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**9)
N = int(input())


def main(s, o, n):
    n += 1
    if n == N:
        print(s)
    else:
        for i in range(97, o + 2):
            main(s + chr(i), max(o, i), n)


main("a", 97, 0)
