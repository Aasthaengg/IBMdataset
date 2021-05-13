#!/usr/bin/env python3
import sys
from collections import defaultdict
# input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))


def main():
    N = INT()
    P = [INT() for _ in range(N)]

    # dp[i] = iを最後とする1づつ連続する増加列の長さ
    dp = [0]*(N+1)

    for i in range(N):
        dp[P[i]] = dp[P[i]-1] + 1
    
    print(N-max(dp))
    return


if __name__ == '__main__':
    main()
