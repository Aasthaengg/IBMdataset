#!/usr/bin/env python3
import sys
import math

def main():
    N = int(input())
    digit = math.floor(math.log10(N))
    c = N // 10**digit
    if N == (1 + c) * 10 ** digit - 1:
        print(9 * digit + c)
    else:
        print(9 * digit + c -1)


if __name__ == '__main__':
    main()
