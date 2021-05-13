def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    s = input().rstrip() + 'T'
    x,y = map(int, input().split())
    # 奇数はy方向, 偶数はx方向
    l = []
    susumu = 0
    for i in range(len(s)):
        if s[i] == 'T':
            l.append(susumu)
            susumu = 0
        else:
            susumu += 1
    b = len(l)
    dp = [[0]*16001 for _ in range(3)]
    dp[0][8000] = 1
    dp[1][8000] = 1
    for i in range(b):
        if i==0:
            dp[2][8000+l[i]] = 1
        elif i%2 == 0:
            for j in range(16000):
                if dp[0][j]:
                    dp[2][j-l[i]] = 1
                    dp[2][j+l[i]] = 1
        elif i%2 == 1:
            for j in range(16000):
                if dp[0][j]:
                    dp[2][j-l[i]] = 1
                    dp[2][j+l[i]] = 1
        dp = dp[1:] + [[0]*16000]
    if b%2 == 0:
        if dp[0][x+8000] == 1 and dp[1][y+8000] == 1:
            print('Yes')
        else:
            print('No')
    else:
        if dp[1][x+8000] == 1 and dp[0][y+8000] == 1:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()