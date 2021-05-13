def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    from math import gcd

    #inf = 10**17
    mod = 10**9 + 7

    n = int(input())
    posi = {}
    nega = {}
    ab_zero = 0
    a_zero = 0
    b_zero = 0

    for _ in range(n):
        a,b = map(int, input().split())
        if a==0 and b==0:
            ab_zero += 1
        elif a==0:
            a_zero += 1
        elif b==0:
            b_zero += 1
        elif a*b > 0:
            a = abs(a)
            b = abs(b)
            g = gcd(a, b)
            po = (a//g, b//g)
            if po in posi:
                posi[po] += 1
            else:
                posi[po] = 1
        else:
            a = abs(a)
            b = abs(b)
            g = gcd(a, b)
            ne = (b//g, a//g)
            if ne in nega:
                nega[ne] += 1
            else:
                nega[ne] = 1
    
    res = pow(2, a_zero, mod) + pow(2, b_zero, mod) - 1
    for k, v in posi.items():
        if k in nega:
            res *= pow(2, v, mod) + pow(2, nega[k], mod) - 1
            res %= mod
            nega.pop(k)
        else:
            res *= pow(2, v, mod)
            res %= mod

    for v in nega.values():
        res *= pow(2, v, mod)
        res %= mod

    res += ab_zero - 1
    print(res%mod)

if __name__ == '__main__':
    main()