import sys

# import bisect
# import numpy as np
from collections import deque
# map(int, sys.stdin.read().split())



def input():
    return sys.stdin.readline().rstrip()


def main():
    mod =998244353
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    dp =[[0]*(S+1) for _ in range(N+1)]
    dp[0][0]=1
    for i in range(0,N):
        for j in range(S+1):
            if A[i]>j:
                dp[i+1][j] =dp[i][j]*2
                dp[i+1][j] %= mod
            else:
                dp[i+1][j] = dp[i][j]*2 + dp[i][j-A[i]]
                dp[i+1][j] %= mod
    print(dp[N][S])
    pass



if __name__ == "__main__":
    main()
