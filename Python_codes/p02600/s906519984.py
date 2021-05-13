import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    x = int(input())
    kyu = 8
    for i in range(400, 1801, 200):
        if i <= x <= i+199:
            print(kyu)
        kyu -= 1
    return 0

if __name__ == "__main__":
    solve()