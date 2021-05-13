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

    n,a,b = map(int, input().split())
    if a > b:
        print(0)
    elif n == 1:
        if a == b:
            print(1)
        else:
            print(0)
    elif n == 2:
        print(1)
    else:
        print((b-a)*(n-2)+1)

if __name__ == '__main__':
    main()