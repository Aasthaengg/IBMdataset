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

    n = int(input())
    s = []
    t = []
    for _ in range(n):
        a,b = input().rstrip().split()
        s.append(a)
        t.append(int(b))
    x = input().rstrip()
    y = s.index(x)
    print(sum(t[y+1:]))

if __name__ == '__main__':
    main()