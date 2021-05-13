import numpy as np
import math
import collections
import fractions
import itertools

def rec(d, val, all):
    all.append(val)
    if d >= 10:
        return
    for j in range(-1, 2):
        add = val % 10 + j
        if add >= 0 and add <= 9:
            rec(d+1, val*10+add, all)

def solve():
    k = int(input())
    all = []
    for i in range(1,10):
        rec(1, i, all)
    all.sort()
    print(all[k-1])
    return 0

if __name__ == "__main__":
    solve()
