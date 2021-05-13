import sys
import collections
import bisect


def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    c = collections.Counter(A)
    sumA = 0
    cKeys = c.keys()
    for cKey in cKeys:
        sumA += c[cKey] % 2
    print(sumA)


if __name__ == '__main__':
    main()
