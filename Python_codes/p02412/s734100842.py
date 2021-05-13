#!/usr/local/env python3

import sys


def main():
    while True:
        count = 0
        n, r = map(int, sys.stdin.readline().split())
        if n == r == 0:
            break
        for n1 in range(1, n-1):
            for n2 in range(n1+1, n):
                for n3 in range(n2+1, n+1):
                    if n1 + n2 + n3 == r:
                        count += 1
        print(count)


if __name__ == '__main__':
    main()