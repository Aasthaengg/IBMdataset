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

    n,c,k = map(int, input().split())
    t = [int(input()) for _ in range(n)]
    t.sort()
    res = 1
    time, hito = t[0], 0
    for i in range(n):
        if t[i] - time > k:
            time = t[i]
            res += 1
            hito = 1
        elif hito + 1 > c:
            time = t[i]
            res += 1
            hito = 1
        else:
            hito += 1

    print(res)

if __name__ == '__main__':
    main()