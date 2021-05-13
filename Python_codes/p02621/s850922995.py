import math
import sys
from collections import Counter
readline = sys.stdin.readline


def main():
    a = int(readline().rstrip())

    print(a + a**2 + a**3)


if __name__ == '__main__':
    main()
