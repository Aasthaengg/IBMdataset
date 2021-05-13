import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import statistics # Pythonのみ
# import string
import unittest
from io import StringIO
import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    l = [0]*(n+1)
    l[n] = (A[n], A[n])
    for i in reversed(range(1, n+1)):
        l[i-1] = (max(math.ceil(l[i][0]/2)+A[i-1], 1), l[i][1]+A[i-1])

    if 1 not in range(l[0][0], l[0][1]+1):
        print(-1)
    else:
        ans = [0]*(n+1)
        ans[0] = 1
        cnt = 1
        for i in range(n):
            ans[i+1] = min((ans[i]-A[i])*2, l[i+1][1])
        print(sum(ans))


resolve()