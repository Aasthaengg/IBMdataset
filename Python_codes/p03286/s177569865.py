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

    if n == 0:
        print('0')
        exit()

    a = 0
    for i in range(1, 40, 2):
        a -= 2**i
    b = n - a
    res = []
    for i in range(40):
        if i%2 == 0:
            if (b>>i) & 1:
                res.append('1')
            else:
                res.append('0')
        else:
            if (b>>i) & 1:
                res.append('0')
            else:
                res.append('1')

    res = res[::-1]
    for i in range(40):
        if res[i] == '1':
            print(''.join(res[i:]))
            exit()

if __name__ == '__main__':
    main()