import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
inf = 10**9

n, k = [0, 0]
w = []


def validate(p):
    c = 0
    for i in range(k):
        s = 0
        while s + w[c] <= p:
            s = s + w[c]
            c = c + 1
            if c == n:
                return True
    return False


def main():
    global n
    global k
    global w
    n, k = map(int, input().split())
    for i in range(n):
        w.append(int(input()))

    # bianry search
    left = 0
    right = 100000 * 10000
    p = right / 2
    while left != right:
        if validate(p):
            right = p
        else:
            left = p + 1
        p = math.floor((left + right) / 2)

    print(p)


if __name__ == '__main__':
    main()

