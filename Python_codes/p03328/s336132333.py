#pypyは内包表記使わない, rstrip注意
#提出前に見返すこと！
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 1000000007

    a, b = map(int, input().split())
    x = b - a
    print(x*(x-1)//2 - a)

if __name__ == '__main__':
    main()