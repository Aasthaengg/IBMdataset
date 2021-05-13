#!/usr/bin/python3
# import bisect
# from collections import Counter, deque, OrderedDict, defaultdict
# from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
# from functools import reduce
# from heapq import heapify, heappop, heappush
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    # https://stackoverflow.com/a/33356284
    import itertools
    
    
    def primes(n):
        """ Input n>=6, Returns a list of primes, 2 <= p < n """
        zero = bytearray([False])
        size = n//3 + (n % 6 == 2)
        sieve = bytearray([True]) * size
        sieve[0] = False
        for i in range(int(n**0.5)//3+1):
            if sieve[i]:
                k = 3*i+1 | 1
                start = (k*k+4*k-2*k*(i & 1))//3
                sieve[(k*k)//3::2*k] = zero*((size - (k*k)//3 - 1) // (2 * k) + 1)
                sieve[start::2*k] = zero*((size - start - 1) // (2 * k) + 1)
        ans = [2, 3]
        poss = itertools.chain.from_iterable(
            itertools.zip_longest(*[range(i, n, 6) for i in (1, 5)]))
        ans.extend(itertools.compress(poss, sieve))
        return ans
    n=int(input())
    p=primes(55555)
    l=[]
    for i in p:
        if i%5==1:
            l.append(i)
    print(*l[:n])

    
resolve()