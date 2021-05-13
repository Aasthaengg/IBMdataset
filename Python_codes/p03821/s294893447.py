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

    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for i in range(n-1, -1, -1):
        a = (ab[i][0]+res) % ab[i][1]
        if a == 0:
            continue
        res += ab[i][1] - a
    print(res)

if __name__ == '__main__':
    main()