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

    N, K = map(int, input().split())
    S = list(input())
    gr = groupby(S)
    cnt = 0
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    for key, group in gr:  # groupはイテレータ。list(group)でリスト化
        """ex.
        0: [0, 0, 0]
        1: [1, 1]
        0: [0, 0, 0]
        1: [1, 1]
        0: [0]
        1: [1]
        """
        cnt += 1
    cut = cnt-1
    while K > 0:
        if cut == 0:
            break
        elif cut >= 2:
            happy += 2
            cut -= 2
        else:
            happy += 1
            cut -= 1
        K -= 1

    print(happy)

resolve()