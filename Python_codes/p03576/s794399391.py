def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n,k = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    x = sorted(xy, key=lambda a: a[0])
    y = sorted(xy, key=lambda a: a[1])

    res = 10**20
    for l in range(n):
        for r in range(l+1, n):
            for b in range(n):
                for t in range(b+1, n):
                    cnt = 0
                    for vx, vy in x[l:r+1]:
                        if y[b][1] <= vy <= y[t][1]:
                            cnt += 1
                        if cnt >= k:
                            res = min(res, (x[r][0]-x[l][0])*(y[t][1]-y[b][1]))
                            break
    print(res)

if __name__ == '__main__':
    main()

