def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    N,K = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0]*(K+1)
    for i in range(1, K+1):
        for j in a:
            if i-j < 0:
                continue
            if dp[i-j] == 0:
                dp[i] = 1
                break
    if dp[K]:
        print('First')
    else:
        print('Second')

if __name__ == '__main__':
    main()