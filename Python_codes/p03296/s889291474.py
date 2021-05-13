#!/usr/bin/env python
from collections import defaultdict, deque
import math
from math import factorial
import fractions
import re

BIGNUM = 10 ** 9 + 7

def main():
    #N, x = map(int, input().split())
    #As = list(map(int, input().split()))
    N = int(input())
    As = list(map(int, input().split()))
    As.append(100000)

    magic_num = 0
    prev = None
    seq = 1
    for a in As:
        if prev is not None:
            if prev == a:
                seq += 1
            else:
                if seq > 1:
                    magic_num += seq // 2
                seq = 1
        prev = a

    print(magic_num)

if __name__ == '__main__':
    main()
