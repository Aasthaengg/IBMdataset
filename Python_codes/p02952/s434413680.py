#!/usr/bin/env python3
import math


def main():
    N = int(input())
    digit = math.floor(math.log10(N)) + 1
    if digit == 1:
        print(N)
    elif digit == 2:
        print(9)
    elif digit == 3:
        print(9 + N - 100 + 1)
    elif digit == 4:
        print(909)
    elif digit == 5:
        print(909 + N - 10000 + 1)
    elif digit == 6:
        print(90909)


if __name__ == '__main__':
    main()
