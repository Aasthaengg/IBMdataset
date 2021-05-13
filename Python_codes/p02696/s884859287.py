import math
import sys
import collections
import bisect


def main():
    a, b, n = map(int, input().split())
    i = max(b - 1 if n >= b else n, 1)
    print(math.floor(a * i / b) - a * math.floor(i / b))


if __name__ == '__main__':
    main()
