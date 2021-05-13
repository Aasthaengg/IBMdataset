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

    a,b,c = map(int, input().split())
    if a%2 == 1 and b%2 == 1 and c%2 == 1:
        print(min(a*b, b*c, c*a))
    else:
        print(0)

if __name__ == '__main__':
    main()