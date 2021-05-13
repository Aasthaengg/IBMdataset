import numpy as np
import functools
import math
import collections
import scipy
import fractions
import itertools

def rle(l):
    hoge = list(set(l))
    huga = []
    for i in hoge:
        huga.append(l.count(i))
    huga.sort()
    return huga

def solve():
    s = list(input())
    t = list(input())
    if rle(s) == rle(t):
        print("Yes")
    else:
        print("No")
    return 0

if __name__ == "__main__":
    solve()
