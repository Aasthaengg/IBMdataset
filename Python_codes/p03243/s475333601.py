import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    n = int(input())
    while True:
        if len(set(str(n))) == 1:
            print(n)
            break
        n += 1
    return 0

if __name__ == "__main__":
    solve()