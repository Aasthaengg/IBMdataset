import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    n = int(readline().rstrip())
    a = [0] * 10100
    for i in range(1, 105):
        for j in range(1, 105):
            for k in range(1, 105):
                m = i ** 2 + j ** 2 + k ** 2 + i * j + j * k + k * i - 1
                if m < 10050:
                    a[m] += + 1
    for s in range(n):
        print(a[s])


if __name__ == '__main__':
    main()
