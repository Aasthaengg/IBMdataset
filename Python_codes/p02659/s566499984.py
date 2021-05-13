import math
import sys
import bisect
readline = sys.stdin.readline


def main():
    a, b = map(float, readline().rstrip().split())
    a = int(a)
    b = round(b * 100)
    print((a * b) // 100)


if __name__ == '__main__':
    main()
