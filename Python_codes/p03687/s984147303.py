import numpy as np
import functools
import math
import scipy
import fractions
import itertools

def rle(s, tar):
    ans = []
    hoge = 0
    for i in range(len(s)):
        if s[i] != tar:
            hoge += 1
        else:
            ans.append(hoge)
            hoge = 0
    ans.append(hoge)
    return ans

def solve():
    s = list(input())
    ele = sorted(list(set(s)))
    le = len(ele)
    n = len(s)
    cost = [0]*le
    for i in range(le):
        cost[i] = max(rle(s, ele[i]))
    print(min(cost))
    return 0

if __name__ == "__main__":
    solve()

