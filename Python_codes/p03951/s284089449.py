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
    s = input().rstrip()
    t = input().rstrip()
    res = 0
    for i in range(n):
        if s[n-(i+1):] == t[:i+1]:
            res = i + 1
    print(n * 2 - res)

if __name__ == '__main__':
    main()