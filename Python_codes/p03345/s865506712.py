import math
import sys
import collections
import bisect


def main():
    a, b, c, k = map(int, input().split())
    print((-1) ** k * (a - b))


if __name__ == '__main__':
    main()
