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

    x, y = map(int, input().split())
    res = 10**10
    if x == -y:
        res = 1
    if x < y:
        res = min(res, y-x)
    if x > y:
        res = min(res, x-y+2)
    if -x < y:
        res = min(res, y+x+1)
    if -x > y:
        res = min(res, -x-y+1)
    print(res)

if __name__ == '__main__':
    main()