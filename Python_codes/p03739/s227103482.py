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

    n = int(input())
    A = list(map(int, input().split()))
    val=0
    ans = 0
    for i in range(len(A)):
        val+=A[i]
        if val>=0 and i%2==0:
            ans+=val+1
            val=-1
        elif val<=0 and i%2==1:
            ans+=abs(val)+1
            val=1
    val=0
    ans2=0
    for i in range(len(A)):
        val+=A[i]
        if val>=0 and i%2==1:
            ans2+=val+1
            val=-1
        elif val<=0 and i%2==0:
            ans2+=abs(val)+1
            val=1


    print(min(ans2,ans))



resolve()