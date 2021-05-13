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
    a = list(map(int, input().split()))
    b = sorted(a)
    res = []
    if abs(b[0]) <= b[-1]:
        x = a.index(b[-1])
        for i in range(n):
            if a[i] < 0:
                res.append([x+1, i+1])
        print(n-1+len(res))
        for i in res:
            print(*i)
        for i in range(n-1):
            print(i+1, i+2)
    else:
        x = a.index(b[0])
        for i in range(n):
            if a[i] > 0:
                res.append([x+1, i+1])
        print(n-1+len(res))
        for i in res:
            print(*i)
        for i in range(n-1, 0, -1):
            print(i+1, i)
    

if __name__ == '__main__':
    main()