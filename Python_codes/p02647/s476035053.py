from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
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
    
    n,k=map(int,input().split())
    A=list(map(int,input().split()))

    for i in range(k):
        B=[0]*(n+1)

        for j in range(n):
            val=A[j]
            B[max(0,j-val)]+=1
            B[min(n,j+val+1)]-=1
        
        B = list(accumulate(B))
        
        A=B[:-1]

        if A==[n]*(n):
            break
    
    

    print(*A)    
    
resolve()