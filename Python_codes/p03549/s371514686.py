import math
import sys
import bisect
readline = sys.stdin.readline


def main():
    n, m = map(int, readline().rstrip().split())
    cnt = 2 ** m
    print((n + m * 18) * cnt * 100)


if __name__ == '__main__':
    main()
