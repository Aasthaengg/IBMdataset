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

    r,g,b,n = map(int, input().split())
    res = 0
    for i in range(3001):
        temp = n - r*i
        for j in range(3001):
            temp2 = temp - g*j
            if temp2>=0 and temp2%b==0:
                res += 1
    print(res)

if __name__ == '__main__':
    main()