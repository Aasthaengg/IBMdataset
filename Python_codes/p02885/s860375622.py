import sys
input = sys.stdin.readline
from itertools import *
from collections import *

INF = float('inf')


def main():
    A, B = map(int, input().split())
    yohaku = A - 2 * B
    print(yohaku if yohaku > 0 else 0)


if __name__ == '__main__':
    main()
