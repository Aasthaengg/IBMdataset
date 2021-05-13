#!/usr/bin/env python3
import sys
from itertools import chain
# from itertools import combinations as comb
# form bisect import bisect_left, bisect_right, insort_left, insort_right
# from collections import Counter
# import numpy as np


def solve(A: int, B: str):
    B = int(B.replace('.', ''))
    ans = A * B
    return ans // 100

def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    A = int(next(tokens))  # type: int
    B = next(tokens)  # type: str
    answer = solve(A, B)
    print(answer)

if __name__ == '__main__':
    main()
