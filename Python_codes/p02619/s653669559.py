def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7
    #epsilon = 10**-9

    d = int(input())
    c = list(map(int, input().split()))
    last = [0]*26
    s = [list(map(int, input().split())) for _ in range(d)]
    res = 0
    for i in range(d):
        t = int(input())
        last[t-1] = i+1
        res += s[i][t-1]
        for j in range(26):
            res -= c[j] * (i+1-last[j])
        print(res)

if __name__ == '__main__':
    main()