def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    mod = 10**9 + 7

    N = int(input())

    #dp[i]:[..]左からi文字目がA,C,G,Tの場合の数
    dp = [[0]*4 for _ in range(N+1)]
    dp[1] = [1]*4
    for i in range(1,N+1):
        for j in range(4):
            dp[i][j] += sum(dp[i-1])
            dp[i][j] %= mod
        #3文字見る
        if i >= 2:
            dp[i][1] -= dp[i-2][0]*1 + dp[i-2][2]*1
            dp[i][2] -= dp[i-2][0]*1
        #4文字見る
        if i >= 3:
            #ACGC ATGC AGGCで×3
            dp[i][1] -= dp[i-3][0]*3
            #GACGはそもそも足してないので余計に引いた分足す
            dp[i][2] += dp[i-3][2]*1

    print(sum(dp[N])%mod)

if __name__ == '__main__':
    main()
