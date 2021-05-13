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
    a,b = map(int, input().split())
    p = list(map(int, input().split()))
    c,d,e = 0,0,0
    for i in range(n):
        if p[i]<=a:
            c += 1
        elif p[i]>b:
            e += 1
        else:
            d += 1
    print(min(c,d,e))

if __name__ == '__main__':
    main()