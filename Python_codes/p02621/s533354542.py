#!/usr/bin/env python3
import sys
from itertools import chain
# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
# import numpy as np


def solve(a: int):
    return a + a*a + a*a*a

def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    a = int(next(tokens))  # type: int
    answer = solve(a)
    print(answer)

if __name__ == '__main__':
    main()
