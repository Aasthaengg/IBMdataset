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

    n,m = map(int, input().split())
    xyz = [list(map(int, input().split())) for _ in range(n)]

    def calc(i, j, k):
        a = []
        for x, y, z in xyz:
            a.append(x*i+y*j+z*k)
        a.sort(reverse=True)
        return sum(a[:m])

    res = 0
    # 基準 0:負 1:正
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            for k in range(-1, 2, 2):
                res = max(res, calc(i, j, k))
    print(res)

if __name__ == '__main__':
    main()