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

    n,m,X,Y = map(int, input().split())
    x = [X] + list(map(int, input().split()))
    y = [Y] + list(map(int, input().split()))
    if max(x) < min(y):
        print('No War')
    else:
        print('War')

if __name__ == '__main__':
    main()