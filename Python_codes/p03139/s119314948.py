import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n, a, b = map(int, readline().rstrip().split())
    print(min(a, b), max(a + b - n, 0))


if __name__ == '__main__':
    main()
