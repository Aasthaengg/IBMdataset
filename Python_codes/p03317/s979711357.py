# import bisect
# from collections import Counter, deque
# import copy
# from fractions import gcd
# from functools import reduce
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline

def resolve():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))

    if N==K:
        print(1)
    else:
        N=N-K
        print(1+-(-N//(K-1)))


resolve()