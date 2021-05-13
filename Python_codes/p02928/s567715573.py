import numpy as np
import functools
import math
import scipy
import fractions
import itertools

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    hoge, huga = 0, 0
    piyo = 10**9+7
    for i in range(n-1):
        for j in range(i, n):
            if a[i] > a[j]:
                hoge += 1
    hoge *= k
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i] > a[j]:
                    huga += 1
    huga *= (k*(k-1))//2
    print((hoge+huga)%piyo)
    return 0

if __name__ == "__main__":
    solve()