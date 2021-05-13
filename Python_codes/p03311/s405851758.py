import numpy as np  # Pythonのみ！
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
    
    N=int(input())
    A=list(map(int,input().split()))
    B=[0]*N
    for i in range(N):
        B[i]=A[i]-(i+1)
    val=np.median(B)

    ans=0
    for i in range(N):
        ans+=abs(val-B[i])
    print(int(ans))

    

    
resolve()