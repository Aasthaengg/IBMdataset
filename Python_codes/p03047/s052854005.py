import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, k = map(int, readline().rstrip().split())
    print(n - k + 1)


if __name__ == '__main__':
    main()
