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

    a = input().rstrip()
    b = input().rstrip()
    c = input().rstrip()
    print(a[0]+b[1]+c[2])


if __name__ == '__main__':
    main()