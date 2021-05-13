from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    A=list(map(int,input().split()))
    cnt=0
    gr = groupby(A)
    for key, group in gr: # groupはイテレータ。list(group)でリスト化  
        """ex.
        0: [0, 0, 0]
        1: [1, 1]
        0: [0, 0, 0]
        1: [1, 1]
        0: [0]
        1: [1]
        """
        cnt+=len(list(group))//2

    
    print(cnt)
        
    


    
resolve()