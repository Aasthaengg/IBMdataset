def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    mod = 10**9 + 7

    n,m = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    dp = [[1]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if t[j-1] == s[i-1]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
            dp[i][j] %= mod
    print(dp[-1][-1])

if __name__ == '__main__':
    main()