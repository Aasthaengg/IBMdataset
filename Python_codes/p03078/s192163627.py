#!/usr/bin/python3
# import bisect
# from collections import Counter, deque, OrderedDict, defaultdict
# from copy import copy, deepcopy # pythonのみ．copyは1次元，deepcopyは多次元．
# from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
# from functools import reduce
from heapq import heapify, heappop, heappush
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
    x,y,z,k=map(int,input().split())
    A=sorted(list(map(int,input().split())),reverse=True)
    B=sorted(list(map(int,input().split())),reverse=True)
    C=sorted(list(map(int,input().split())),reverse=True)

    h=[]
    heapify(h)
    ac,bc,cc=0,0,0

    heappush(h, (-(A[ac]+B[bc]+C[cc]), ac,bc,cc))
    checked=set()

            
    checked.add((-(A[ac]+B[bc]+C[cc]),ac,bc,cc))


    for _ in range(k):
        (p,ac,bc,cc)=heappop(h)
        print(-p)
        if ac+1<x:
            if (-(A[ac+1]+B[bc]+C[cc]), ac+1,bc,cc) not in checked:
                heappush(h, (-(A[ac+1]+B[bc]+C[cc]), ac+1,bc,cc))
                checked.add((-(A[ac+1]+B[bc]+C[cc]), ac+1,bc,cc))

        if bc+1<y:  
                        
            if (-(A[ac]+B[bc+1]+C[cc]), ac,bc+1,cc) not in checked:
                heappush(h, (-(A[ac]+B[bc+1]+C[cc]), ac,bc+1,cc))
                checked.add((-(A[ac]+B[bc+1]+C[cc]), ac,bc+1,cc))
        if cc+1<z:
            if (-(A[ac]+B[bc]+C[cc+1]), ac,bc,cc+1) not in checked:
                heappush(h, (-(A[ac]+B[bc]+C[cc+1]), ac,bc,cc+1))
                checked.add((-(A[ac]+B[bc]+C[cc+1]), ac,bc,cc+1))




    


    


    
resolve()