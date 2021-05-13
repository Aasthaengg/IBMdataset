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
    #mod = 10**9 + 7
    #epsilon = 10**-9

    d = int(input())
    c = list(map(int, input().split()))
    last = [0]*26
    s = [list(map(int, input().split())) for _ in range(d)]
    res = []

    def scoring(last, n):
        score = -10**20
        # 開催するコンテスト
        for i in range(26):
            ans = 0
            ans += s[n][i]
            for j in range(26):
                if i == j:
                    continue
                ans -= c[j] * (n+1-last[j])
            if score < ans:
                score = ans
                contest = i

        return contest, last

    for i in range(d):
        contest, last = scoring(last, i)
        last[contest] = i + 1
        res.append(contest+1)

    for i in res:
        print(i)

if __name__ == '__main__':
    main()