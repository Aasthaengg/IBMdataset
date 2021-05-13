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

    a,b =map(int, input().split())
    if a%3==0:
        print('Possible')
        exit()
    if b%3==0:
        print('Possible')
        exit()
    if (a+b)%3==0:
        print('Possible')
        exit()
    print('Impossible')

if __name__ == '__main__':
    main()