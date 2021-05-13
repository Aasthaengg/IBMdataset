import sys
import collections
import bisect
import math
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    A = sorted(list(map(int, readline().rstrip().split())))
    a = sorted(A[0:n-1] * 2, reverse=True)
    print(max(A) + sum(a[0:n-2]))


if __name__ == '__main__':
    main()
