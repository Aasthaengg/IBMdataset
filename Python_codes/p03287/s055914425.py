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

    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(accumulate(a))
    for i in range(n):
        b[i] %= m
    b = [0] + b
    c = Counter(b)
    res = 0
    for k, v in c.items():
            res += v*(v-1)//2
    print(res)
    
if __name__ == '__main__':
    main()