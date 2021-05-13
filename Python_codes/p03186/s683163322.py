#!/usr/bin/env python
from collections import defaultdict, deque
import math
from math import factorial
import re

BIGNUM = 10 ** 9 + 7

def main():
    A, B, C = map(int, input().split())

    if C <= A+B+1:
        print(C+B)
    else:
        print(B+(B+A)+1)

if __name__ == '__main__':
    main()
