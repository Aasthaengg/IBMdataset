# import math
# import itertools
# from collections import deque
# from collections import defaultdict
# import heapq
import sys
# import numpy as np
# from scipy.special import comb

sys.setrecursionlimit(100000)
INF = 100100100

N = int(input())
memo = [-1] * (N + 1)
memo[0] = 0


def f(n):

    # 0なら終了
    if n == 0:
        return 0

    # メモされてたら終了
    if not memo[n] == -1:
        return memo[n]

    ans = INF

    # 9
    for i in range(1, n):
        if 9 ** i > n:
            break
        ans = min(ans, f(n - 9**i) + 1)

    # 6
    for i in range(1, n):
        if 6 ** i > n:
            break
        ans = min(ans, f(n - 6**i) + 1)

    # 1
    ans = min(ans, f(n - 1) + 1)

    # メモ
    memo[n] = ans
    return ans


def main():

    print(f(N))


if __name__ == '__main__':
    main()
