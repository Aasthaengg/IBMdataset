def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    def digsum(n):
        res = 0
        while n:
            res += n%10
            n //= 10
        return res
    res = 1000000
    for i in range(1, n):
        a = i
        b = n-i
        res = min(res, digsum(a)+digsum(b))
    print(res)

if __name__ == '__main__':
    main()