import bisect
# from collections import Counter, deque
# from copy import copy, deepcopy
# from fractions import gcd
# from functools import reduce
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np
# from operator import xor
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline

def resolve():
    N=int(input())
    A=sorted(list(map(int,input().split())))
    B=list(map(int,input().split()))
    C=sorted(list(map(int,input().split())))

    cnt=0
    for i in B:
        a=bisect.bisect_left(A,i)
        c=N-bisect.bisect_right(C,i)
        cnt+=a*c

    print(cnt)





resolve()