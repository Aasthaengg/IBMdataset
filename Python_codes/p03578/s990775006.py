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
    d = list(map(int, input().split()))
    m = int(input())
    t = list(map(int, input().split()))
    dc = Counter(d)
    tc = Counter(t)
    for k, v in tc.items():
        if dc[k]<v:
            print('NO')
            break
    else:
        print('YES')

if __name__ == '__main__':
    main()