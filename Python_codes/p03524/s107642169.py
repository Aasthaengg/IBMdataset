import sys
from operator import itemgetter
import collections
import math


def r(s):
    a = s.count('a')
    b = s.count('b')
    c = s.count('c')
    ma = max(a, b, c)
    mn = min(a, b, c)
    return 'YES' if 1 >= ma - mn else 'NO'


def main():
    input = sys.stdin.readline
    s = input()
    print(r(s))


if __name__ == '__main__':
    main()
