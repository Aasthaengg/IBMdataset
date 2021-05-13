import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    r = input()
    if r == 'RRR':
        print(3)
    elif r == 'RRS' or r == 'SRR':
        print(2)
    elif r == 'RSR' or r == 'RSS' or r =='SSR' or r =='SRS':
        print(1)
    elif r == 'SSS':
        print(0)
    return 0

if __name__ == "__main__":
    solve()