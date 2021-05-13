from numba import jit
@jit
def Sum_divisors():
    n,ans=int(input()),0
    for i in range(1, n+1):
        for j in range(i, n+1, i):ans+=j
    print(ans)

Sum_divisors()
