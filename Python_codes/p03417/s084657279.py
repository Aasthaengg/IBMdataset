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

    N, M = map(int, input().split())
    if N==1 and M==1:
        print(1)
    elif N==1 or M==1:
        print(max(N, M)-2)
    else:
        print(N*M - ((N+M)*2 - 4))



if __name__ == '__main__':
    main()