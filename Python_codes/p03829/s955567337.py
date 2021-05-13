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

    N,A,B = map(int, input().split())
    X = list(map(int, input().split()))
    res = 0
    for i in range(N-1):
        if (X[i+1]-X[i])*A>B:
            res += B
        else:
            res += (X[i+1]-X[i])*A
    print(res)

if __name__ == '__main__':
    main()