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

    a = 0
    for i in range(1, 40, 2):
        a -= 2**i
    b = n - a

    res = 0
    for i in range(40):
        if i%2 == 0:
            if (b>>i) & 1:
                res += 1<<i
        else:
            if ((b>>i) & 1) == 0:
                res += 1<<i

    print('{:b}'.format(res))

if __name__ == '__main__':
    main()