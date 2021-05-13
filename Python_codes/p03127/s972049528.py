import sys
from math import gcd
from functools import reduce

readline = sys.stdin.buffer.readline


def main():
    N = int(readline())
    A = map(int, readline().split())

    print(reduce(gcd, A))
    return


if __name__ == '__main__':
    main()
