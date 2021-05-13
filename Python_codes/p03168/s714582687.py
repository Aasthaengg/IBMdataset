#コインで裏をn回出す確率

def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    from math import floor, ceil
    #from operator import itemgetter

    #mod = 1000000007

    N = int(input())
    p = tuple(map(float, input().split()))

    #dp[j]:裏がj枚でる確率
    dp = [1] + [0]*(N//2)
    for i in range(N):
        for j in range(i+1, -1, -1):
            if j==0:
                dp[j] = dp[j]*p[i]
            elif j<=(N//2):
                dp[j] = dp[j-1]*(1-p[i]) + dp[j] * p[i]
    res = sum(dp)
    print('{:.9f}'.format(res))

if __name__ == '__main__':
    main()