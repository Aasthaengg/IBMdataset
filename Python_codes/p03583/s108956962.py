import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    for h in range(1, 3501):
        for n in range(1, 3501):
            numerator = 4 * h * n - N * (h + n)
            denominator = N * h * n
            if (numerator >= 1) and (numerator <= denominator):
                if denominator % numerator == 0:
                    w = denominator // numerator
                    return print(h, n, w)


if __name__ == '__main__':
    main()
