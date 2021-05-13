def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    s = input().rstrip()
    res = 0
    for i in s:
        if i=='C' and res==0:
            res += 1
        if i=='F' and res==1:
            res += 1
    if res==2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()