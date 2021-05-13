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

    s = input().rstrip()
    a = 0
    res = 0
    for i in s:
        if i == 'S':
            a += 1
        else:
            if a <= 0:
                res += 1
            else:
                a -= 1
    print(res+a)

if __name__ == '__main__':
    main()