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

    n,k = map(int, input().split())
    a = list(map(int, input().split()))

    #ibit目が0である数と1である数
    zero, one = [0]*40, [0]*40

    for i in range(n):
        for bit in range(40):
            if (a[i]>>bit) & 1:
                one[bit] += 1
            else:
                zero[bit] += 1
    #貪欲な方
    res1 = 0
    #貪欲じゃない方
    res2 = 0
    flag = 0
    for i in range(39, -1, -1):
        if flag == 0:
            if (k>>i) & 1:
                res1 += 2**i * one[i]
                res2 += 2**i * zero[i]
                flag = 1
            else:
                res1 += 2**i * one[i]
                res2 += 2**i * one[i]
        else:
            if (k>>i) & 1:
                res1 = max(res1 + 2**i * max(one[i], zero[i]), res2 + 2**i * one[i])
                res2 += 2**i * zero[i]
            else:
                res1 += 2**i * max(one[i], zero[i])
                res2 += 2**i * one[i]
    print(max(res1, res2))

if __name__ == '__main__':
    main()