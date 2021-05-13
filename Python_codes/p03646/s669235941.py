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

    k = int(input())
    n = 50
    s = k // n
    amari = k % n
    res = list(range(n-1, -1, -1))
    for i in range(n):
        res[i] += s
    cnt = 0
    while cnt < amari:
        cnt += 1
        res[-cnt] += n+1
        for i in range(n):
            res[i] -= 1
    print(n)
    print(*res)

if __name__ == '__main__':
    main()