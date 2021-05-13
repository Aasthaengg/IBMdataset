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
    res = 0
    cnt = 0
    while cnt < n-1:
        if a[cnt] == a[cnt+1]:
            res += 1
            cnt += 2
        else:
            cnt += 1
    print(res)

if __name__ == '__main__':
    main()