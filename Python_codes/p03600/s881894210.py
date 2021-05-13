def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 1000000007

    N=int(input())
    dp=[list(map(int, input().split())) for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dp[i][j]>dp[i][k]+dp[k][j]:
                    print(-1)
                    exit()
    #dp[i][j]=dp[i][k]+dp[k][j] が成り立つ時調べる？
    res = 0
    for i in range(N-1):
        for j in range(i+1, N):
            for k in range(N):
                if k==i or k == j:
                    continue
                if dp[i][j]==dp[i][k]+dp[k][j]:
                    break
            else:
                res += dp[i][j]
    print(res)


if __name__ == '__main__':
    main()