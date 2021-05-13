import sys
import collections
import bisect


def main():
    a, b, c = map(int, input().split())
    print(b + min(a + b + 1, c))


if __name__ == '__main__':
    main()
