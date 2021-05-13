import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    a, b = input().split()
    n = int(a+b)
    if math.sqrt(n) % 1 == 0:
        print("Yes")
    else:
        print("No")
    return 0

if __name__ == "__main__":
    solve()