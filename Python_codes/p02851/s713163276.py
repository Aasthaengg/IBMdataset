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

    n,k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    a = list(accumulate(a))
    d = {}
    res = 0
    for i in range(n+1):
        b = (i - a[i]) % k
        if i - k < 0:
            if b not in d:
                d[b] = 1
            else:
                res += d[b]
                d[b] += 1
        else:
            j = i - k
            c = (j - a[j]) % k
            d[c] -= 1
            if b not in d:
                d[b] = 1
            else:
                res += d[b]
                d[b] += 1
    print(res)

if __name__ == '__main__':
    main()