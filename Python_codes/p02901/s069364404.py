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

    inf = 10**17
    #mod = 10**9 + 7

    n,m = map(int, input().split())
    # key[i]:10進数でiを開けれる鍵の値段
    key = []
    for _ in range(m):
        a,b = map(int, input().split())
        c = list(map(int, input().split()))
        binary = 0
        for i in c:
            binary += 2**(i-1)
        key.append((binary, a))

    # dp[i]:10進数で宝iを開けてる時の最小値段
    dp = [inf]*(1<<n)
    dp[0] = 0
    for i, a in key:
        for s in range(1<<n):
            if (i|s) == s:
                continue
            dp[i|s] = min(dp[i|s], dp[s]+a)
    print(dp[-1] if dp[-1] != inf else -1)

if __name__ == '__main__':
    main()
