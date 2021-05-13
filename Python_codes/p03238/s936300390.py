def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    if n==1:
        print('Hello World')
        exit()
    else:
        a = int(input())
        b = int(input())
        print(a+b)

if __name__ == '__main__':
    main()