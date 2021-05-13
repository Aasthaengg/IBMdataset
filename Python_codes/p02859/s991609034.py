# coding: utf-8
import sys


def main(argv=sys.argv):

    r = int(input())

    pai = 3

    times = (r ** 2 * pai) // (1 ** 2 * pai)

    print(times)

    return 0


if __name__ == '__main__':
    sys.exit(main())
