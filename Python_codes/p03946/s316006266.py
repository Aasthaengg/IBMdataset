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

    n,t = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0]*n
    b[-1] = a[-1]
    for i in range(n-2, 0, -1):
        if b[i+1] < a[i]:
            b[i] = a[i]
        else:
            b[i] = b[i+1]
    res = 0
    temp = 0
    for i in range(n-1):
        if temp < b[i+1]-a[i]:
            temp = b[i+1]-a[i]
            res = 1
        elif temp == b[i+1]-a[i]:
            res += 1
    print(res)

if __name__ == '__main__':
    main()