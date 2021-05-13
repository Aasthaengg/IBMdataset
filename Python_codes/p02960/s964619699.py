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

    s = str(input())
    ls = len(s)
    dp = [[0]*13 for _ in range(ls+1)]
    dp[0][0] = 1
    MOD = 10**9+7

    for i in range(ls):
        for j in range(13):
            if s[i] == '?':
                for k in range(10):
                    dp[i+1][(j*10+k) % 13] += dp[i][j]
                    dp[i+1][(j*10+k) % 13] %= MOD
            else:
                dp[i+1][(j*10+int(s[i])) % 13] += dp[i][j]
                dp[i+1][(j*10+int(s[i])) % 13] %= MOD

    print(dp[ls][5])


resolve()