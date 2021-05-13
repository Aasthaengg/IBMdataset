import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        print(a*b)
    else:
        print(-1)
    return 0

if __name__ == "__main__":
    solve()