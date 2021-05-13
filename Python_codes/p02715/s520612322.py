#MLE注意！

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
    mod = 10**9 + 7

    n,k = map(int, input().split())
    res = 0
    d = [0]*k
    for i in range(k, 0, -1):
        d[i-1] = pow((k//i), n, mod)
        for j in range(2, (k//i)+1):
            d[i-1] -= d[i*j-1]
        res += i * d[i-1] % mod
    print(res%mod)

if __name__ == '__main__':
    main()