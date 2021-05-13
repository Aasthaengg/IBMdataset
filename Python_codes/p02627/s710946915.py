#!/usr/bin/env python3
import sys
from itertools import chain
# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
# import numpy as np


def solve(c):
    if c.lower() == c:
        return 'a'
    else:
        return 'A'

def main():
    c = input()
    answer = solve(c)
    print(answer)

if __name__ == '__main__':
    main()
