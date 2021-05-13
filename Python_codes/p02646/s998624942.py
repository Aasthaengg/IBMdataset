import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
    a, v = map(int, readline().rstrip().split())
    b, w = map(int, readline().rstrip().split())
    t = int(readline().rstrip())
    if v <= w:
        print('NO')
        return
    print('YES' if abs(b - a) / (v - w)
          <= t else 'NO')


if __name__ == '__main__':
    main()
