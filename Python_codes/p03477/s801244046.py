# coding: utf-8
import sys


def main(argv=sys.argv):

    a, b, c, d = map(int, input().split(' '))

    if (a + b) == (c + d):
        print('Balanced')
    elif (a + b) > (c + d):
        print('Left')
    elif (a + b) < (c + d):
        print('Right')

    return 0


if __name__ == '__main__':
    sys.exit(main())
