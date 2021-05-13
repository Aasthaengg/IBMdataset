import numpy as np
import functools
import math
import scipy
import fractions
import itertools
 
def solve():
    k, t = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(0, max(a)-(sum(a)-max(a))-1))
    return 0

if __name__ == "__main__":
    solve()