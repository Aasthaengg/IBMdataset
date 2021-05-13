import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    a, b, c = map(int, input().split())
    if any([i%2==0 for i in (a, b, c)]):
        print(0)
    else:
        print(min(a*b, b*c, c*a))
    return 0

if __name__ == "__main__":
    solve()