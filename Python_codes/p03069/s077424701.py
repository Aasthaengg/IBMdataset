import sys, math
from functools import lru_cache
from collections import defaultdict, Counter
import bisect
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N = ii()
    S = input()
    dp = [0]*(N+1)
    dp[0] = S.count('.')
    for i in range(N):
        dp[i+1] = dp[i]-1 if S[i] == '.' else dp[i]+1
    print(min(dp))

if __name__ == '__main__':
    main()
