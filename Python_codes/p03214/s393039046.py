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
    b = sum(a)/n
    diff = 10000
    res = 0
    for i in range(n):
        if diff>abs(b-a[i]):
            diff = abs(b-a[i])
            res = i
    print(res)

if __name__ == '__main__':
    main()