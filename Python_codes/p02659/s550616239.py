import sys
from decimal import *
import math

input = sys.stdin.readline


def main():
    A, B = map(Decimal, input().split())
    print(math.floor(A*B))


if __name__ == '__main__':
    main()
