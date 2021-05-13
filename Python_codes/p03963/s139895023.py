# import bisect
# import copy
# import fractions
# import math
# import numpy as np
# from collections import Counter, deque
# from itertools import accumulate,permutations, combinations,combinations_with_replacement,product

def resolve():
    N,K=map(int,input().split())
    val=K
    for i in range(2,N+1):
        val*=(K-1)
    print(val)

resolve()