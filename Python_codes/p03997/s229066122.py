# coding: utf-8
import sys


def main(argv=sys.argv):

    top = int(input())
    bottom = int(input())
    height = int(input())

    print((top + bottom) * height // 2)

    return 0


if __name__ == '__main__':
    sys.exit(main())
