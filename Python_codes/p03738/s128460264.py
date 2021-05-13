# import bisect
# import copy
# import fractions
# import math
# import numpy as np
# from collections import Counter, deque
# from itertools import accumulate,permutations, combinations,combinations_with_replacement,product

def resolve():
    A=int(input())
    B=int(input())
    print('GREATER' if A>B else 'LESS' if A<B else 'EQUAL')

resolve()