import sys
import math 
ni = lambda: int(ns())
na = lambda: list(map(int, input().split()))
ns = lambda: input()
N,K = na()


if K==1:
    print(0)
else:
    print(N-K)