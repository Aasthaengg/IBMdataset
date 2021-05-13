import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    res = []
    while N != 0:
        r = N % 2
        if r < 0:
            r += 2
        N = (N - r) // (-2)
        res += [str(r)]
    res = res[::-1]
    if len(res) == 0:
        print(0)
    else:
        print(''.join(res))


if __name__ == '__main__':
    main()
