import numpy as np
import math
import scipy
import itertools

def solve():
    n, a, b = map(int, input().split())
    if a > b:
        print(0)
    elif n == 1:
        if a == b:
            print(1)
        else:
            print(0)
    else:
        print((b*(n-1)+a)-(a*(n-1)+b)+1)
    return 0

if __name__ == "__main__":
    solve()

