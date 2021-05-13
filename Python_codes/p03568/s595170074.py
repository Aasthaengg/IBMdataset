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
    a = list(map(int, input().split()))
    res = 1
    for i in range(n):
        if a[i]%2 == 1:
            res *= 1
        else:
            res *= 2
    print(3**n-res)

if __name__ == '__main__':
    main()