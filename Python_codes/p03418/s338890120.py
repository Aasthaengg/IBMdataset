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
    if k == 0:
        print(n**2)
        exit()

    res = 0
    for b in range(1, n+1):
        if k >= b:
            continue
        res += (b-k) * ((n+1) // b)
        res += max(((n+1)%b)-k, 0)
    print(res)

if __name__ == '__main__':
    main()