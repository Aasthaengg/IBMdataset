from collections import deque
from itertools import product
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def read():
    N, K = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, K, A


def solve(N, K, A):
    # 先手が勝つ: True, 先手が負ける: False
    dp = [False for i in range(K+1)]
    # 石が残りmin(A)未満のとき、操作不可のため負け
    for i in range(min(A)):
        dp[i] = False
    for i in range(min(A), K+1):
        for a in A:
            if i - a >= 0:
                dp[i] |= not dp[i - a]
    return 'First' if dp[K] else 'Second'


if __name__ == "__main__":
    inputs = read()
    print("%s" % solve(*inputs))
