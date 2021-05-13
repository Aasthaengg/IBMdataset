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

    h,w = map(int, input().split())
    d = []
    for _ in range(h):
        d.append(list(map(int, input().split())))
    
    res = []
    for i in range(h):
        for j in range(w):
            if j == w-1 and i < h-1:
                if d[i][j]%2 == 1:
                    res.append([i+1, j+1, i+2, j+1])
                    d[i+1][j] += 1
                continue
            if d[i][j]%2 == 1 and j < w-1:
                res.append([i+1, j+1, i+1, j+2])
                d[i][j+1] += 1
    print(len(res))
    for i in res:
        print(*i)

if __name__ == '__main__':
    main()