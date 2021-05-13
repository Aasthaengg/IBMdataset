# import bisect
# import copy
# import fractions
# import math
# import numpy as np
# from collections import Counter, deque
# from itertools import accumulate,permutations, combinations,combinations_with_replacement,product

def resolve():

    n=int(input())
    k=int(input())
    val=1
    for i in range(n):
        val=min(val*2,k+val)
    print(val)

resolve()