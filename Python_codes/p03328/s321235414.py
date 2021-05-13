# import bisect
# import copy
# import fractions
# import math
# import numpy as np
# from collections import Counter, deque
# from itertools import accumulate,permutations, combinations,combinations_with_replacement,product

def resolve():
    a, b = map(int, input().split())
    dif = b - a
    print((1 + dif) * dif // 2 - b)


resolve()