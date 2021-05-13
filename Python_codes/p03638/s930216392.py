def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    from math import floor, ceil
    #from operator import itemgetter

    #mod = 1000000007

    H,W = map(int, input().split())
    N = int(input())
    a = list(map(int, input().split()))
    res = []
    for i in range(N):
        for _ in range(a[i]):
            res.append(i+1)
    for i in range(H):
        if  i%2==0:
            b = res[i*W:(i+1)*W]
            print(' '.join(map(str, b)))
        else:
            b = res[i*W:(i+1)*W]
            b = b[::-1]
            print(' '.join(map(str, b)))
if __name__ == '__main__':
    main()