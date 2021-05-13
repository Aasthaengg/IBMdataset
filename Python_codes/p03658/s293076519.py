# import bisect
# import copy
# import fractions
# import math
# import numpy as np
# from collections import Counter, deque
# from itertools import accumulate,permutations, combinations,combinations_with_replacement,product

def resolve():

    N,K=map(int,input().split())
    L=sorted(list(map(int,input().split())),reverse=True)

    print(sum([L[i] for i in range(K)]))


resolve()