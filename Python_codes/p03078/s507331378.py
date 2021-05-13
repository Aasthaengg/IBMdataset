def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    x,y,z,n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort(reverse=1)
    b.sort(reverse=1)
    c.sort(reverse=1)
    res = []
    hq = [[-(a[0]+b[0]+c[0]), 0, 0, 0]]
    heapq.heapify(hq)
    check = set([(0, 0, 0)])
    for _ in range(n):
        cost, i, j, k = heapq.heappop(hq)
        res.append(-cost)
        if i+1<x and not (i+1, j, k) in check:
            heapq.heappush(hq, [-(a[i+1]+b[j]+c[k]), i+1, j, k])
            check.add((i+1, j, k))
        if j+1<y and not (i, j+1, k) in check:
            heapq.heappush(hq, [-(a[i]+b[j+1]+c[k]), i, j+1, k])
            check.add((i, j+1, k))
        if k+1<z and not (i, j, k+1) in check:
            heapq.heappush(hq, [-(a[i]+b[j]+c[k+1]), i, j, k+1])
            check.add((i, j, k+1))
    for i in res:
        print(i)

if __name__ == '__main__':
    main()