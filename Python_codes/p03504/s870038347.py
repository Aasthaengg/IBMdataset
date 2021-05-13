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

    n,c = map(int, input().split())
    stc = [list(map(int, input().split())) for _ in range(n)]
    rokuga = [[0]*c for _ in range(2*10**5+10)]

    for s,t,ch in stc:
        for i in range(int((s-0.5)*2), 2*t):
            rokuga[i][ch-1] = 1
    
    res = 0
    for i in range(1, 2*10**5+10):
        res = max(res, sum(rokuga[i]))
    print(res)

if __name__ == '__main__':
    main()

