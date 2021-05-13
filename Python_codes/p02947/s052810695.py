import sys
import collections
import bisect


def main():
    n = int(input())
    s = [''.join(sorted(list(input()))) for _ in range(n)]
    c = collections.Counter(s)
    cVals = c.values()
    cSum = 0
    for cVal in cVals:
        cSum += cVal * (cVal - 1) // 2
    print(cSum)


if __name__ == '__main__':
    main()
