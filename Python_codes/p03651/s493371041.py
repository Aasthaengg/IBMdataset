import numpy as np
import functools
import math
import scipy
import fractions
import itertools

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    g = a[0]
    for i in range(1, n):
        g = fractions.gcd(g, a[i])
    if k <= max(a) and k % g == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    return 0

if __name__ == "__main__":
    solve()

