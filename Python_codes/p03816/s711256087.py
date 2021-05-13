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
    A = list(map(int, input().split()))
    a = len(set(A))
    res = len(A)-a
    if res%2==0:
        print(a)
    else:
        print(a-1)

if __name__ == '__main__':
    main()