#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]


def main():
    def f(n):
        return n // x + 1

    a, b, x = map(int, input().split())
    print(f(b) - f(a - 1))


if __name__ == '__main__':
    main()
