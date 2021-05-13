import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    s = list(readline().rstrip())
    sumS = 0
    m = s.count('B')
    for i in range(len(s) - 1):
        if s[i] == 'B':
            sumS += (len(s) - m) - i
            m -= 1
    print(sumS)


if __name__ == '__main__':
    main()
