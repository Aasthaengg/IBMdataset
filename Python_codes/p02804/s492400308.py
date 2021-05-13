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
    mod = 10**9 + 7

    max_n = 10**5
    fac, inv = [1]*(max_n+1), [0]*(max_n+1)
    for i in range(2, max_n+1):
        fac[i] = fac[i-1] * i % mod
    inv[-1] = pow(fac[-1], mod-2, mod)
    for i in range(max_n, 0, -1):
        inv[i-1] = inv[i] * i % mod

    def ncr(n, r):
        return fac[n]*inv[r]*inv[n-r]%mod

    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    res_max,res_min = 0, 0
    for i in range(k-1, n):
        temp = ncr(i, k-1)
        res_max += a[i]*temp
        res_min += a[-(i+1)]*temp

    print((res_max - res_min)%mod)

if __name__ == '__main__':
    main()