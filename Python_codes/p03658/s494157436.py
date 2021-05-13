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

    n,k =map(int, input().split())
    l = list(map(int, input().split()))
    l = sorted(l, reverse=1)
    res = 0
    for i in range(k):
        res += l[i]
    print(res)
if __name__ == '__main__':
    main()