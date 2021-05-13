import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    a, b = map(int, input().split())
    if a*b % 2 == 0:
        print("Even")
    else:
        print("Odd")
    return 0

if __name__ == "__main__":
    solve()
