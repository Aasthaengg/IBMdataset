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

    a,b,k = map(int, input().split())
    turn = 0
    while k > 0:
        k -= 1
        if turn == 0:
            if a%2 == 1:
                a -= 1
            a //= 2
            b += a
        else:
            if b%2 == 1:
                b -= 1
            b //= 2
            a += b
        turn ^= 1
    print(a, b)

if __name__ == '__main__':
    main()