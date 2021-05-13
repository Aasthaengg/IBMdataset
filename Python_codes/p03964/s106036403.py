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

    n = int(input())
    at = [list(map(int, input().split())) for _ in range(n)]
    x, y = at[0]
    for i in range(1, n):
        nx, ny = at[i]
        if nx >= x and ny >= y:
            x = nx
            y = ny
        else:
            a = max((x+nx-1)//nx, (y+ny-1)//ny)
            x = nx * a
            y = ny * a
    print(x+y)

if __name__ == '__main__':
    main()