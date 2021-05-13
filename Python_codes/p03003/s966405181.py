import sys
from collections import Counter, deque, defaultdict
from itertools import accumulate, permutations, combinations, takewhile, compress, cycle

# from functools import reduce
# from math import ceil, floor, log10, log2, factorial

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

# N = int(input())
# A = [int(x) for x in input().split()]
# V = [[0] * 100 for _ in range(100)]
# A = [int(input()) for _ in range(N)]

def main():
    """"ここに今までのコード"""
    N, M = [int(x) for x in input().split()]
    S = [int(x) for x in input().split()]
    T = [int(x) for x in input().split()]

    DP = [[0] * (M + 1) for _ in range(N + 1)]
    DP[0] = [1] * (M + 1)
    for n in range(1, N + 1):
        DP[n][0] = DP[n - 1][0]
        for m in range(1, M + 1):
            DP[n][m] = DP[n][m - 1] + DP[n - 1][m] - DP[n - 1][m - 1]
            DP[n][m] %= MOD
            if S[n - 1] == T[m - 1]:
                DP[n][m] += DP[n - 1][m - 1]
                DP[n][m] %= MOD
    print(DP[n][m])


if __name__ == '__main__':
    main()

