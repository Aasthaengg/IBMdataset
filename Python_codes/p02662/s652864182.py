#!/usr/bin/env python3
import sys
import numpy as np
def input(): return sys.stdin.readline().rstrip()


def main():
    n, s = map(int, input().split())
    A = list(map(int, input().split()))
    mod = 998244353
    dp = np.zeros(3001, dtype=np.int64)
    dp[0] = 1
    for AA in A:
        dp = dp*2+np.concatenate([np.zeros(AA, dtype=np.int64), dp[:3001-AA]])
        dp %= mod
    print(dp[s])





if __name__ == '__main__':
    main()
