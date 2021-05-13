def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math

    #inf = 10**17
    mod = 10**9 + 7

    l = input().rstrip()
    n = len(l)

    # dp[i]:上からi+1桁目まで見ている
    # l以下が確定している場合の数
    dp1 = [0]*n
    # lに沿ってる場合の数
    dp2 = [0]*n
    
    # 先頭は1で固定されているので
    dp1[0] = 1
    dp2[0] = 2
    
    for i in range(1, n):
        if l[i] == '1':
            dp1[i] = (dp1[i-1] * 3 + dp2[i-1]) % mod
            dp2[i] = dp2[i-1] * 2 % mod
        else:
            dp1[i] = dp1[i-1] * 3 % mod
            dp2[i] = dp2[i-1]
    print((dp1[-1]+dp2[-1]) % mod)

if __name__ == '__main__':
    main()