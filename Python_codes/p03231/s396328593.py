import fractions
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
    def main():
        N, M = map(int, input().split())
        S = str(input())
        T = str(input())

        lcm = N * M // fractions.gcd(N, M)
        NN = lcm // N
        MM = lcm // M

        lcm2 = NN * MM // fractions.gcd(NN, MM)
        i = 0
        ans = lcm
        while True:
            if lcm2 * i // NN < N and lcm2 * i // MM < M:
                if S[lcm2 * i // NN] != T[lcm2 * i // MM]:
                    ans = -1
                i += 1
            else:
                return ans

    print(main())


resolve()