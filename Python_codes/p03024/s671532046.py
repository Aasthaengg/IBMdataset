import math
import sys
import collections
import bisect
readline = sys.stdin.readline


def main():
     print('YES' if list(readline().rstrip()).count('x') < 8 else 'NO')

if __name__ == '__main__':
    main()
