#pypyは内包表記使わない
def main():
    import sys
    #input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    from math import floor, ceil
    #from operator import itemgetter

    #mod = 1000000007

    N = int(input())
    res = 0
    for _ in range(N):
        l, r = map(int, input().split())
        res += r-l+1
    print(res)

if __name__ == '__main__':
    main()