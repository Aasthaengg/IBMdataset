import numpy as np
import functools
import math
import scipy
import fractions
import itertools
 
def solve():
    x = input()
    a, b = 0, 0
    for i in x:
        if i == "S":
            a += 1
        else:
            if a == 0:
                b += 1
            else:
                a -= 1
    print(a + b)
    return 0

if __name__ == "__main__":
    solve()