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
    res = 0
    while True:
        if a%2 == 0 and b%2 == 0 and c%2 == 0:
            a,b,c = (b+c)//2, (a+c)//2, (a+b)//2
            res += 1
        else:
            print(res)
            break
        if a == b == c:
            print(-1)
            break

if __name__ == '__main__':
    main()

