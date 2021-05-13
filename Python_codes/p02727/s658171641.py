import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    x, y, a, b, c = map(int, input().split())
    print(sum(sorted((sorted(list(map(int, input().split())), reverse=True)[0:x] + sorted(list(map(int, input(
    ).split())), reverse=True)[0:y] + sorted(list(map(int, input().split())), reverse=True)), reverse=True)[0:(x + y)]))


if __name__ == '__main__':
    main()
