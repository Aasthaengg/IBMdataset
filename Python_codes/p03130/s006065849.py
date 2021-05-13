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

    a,b = map(int, input().split())
    c,d = map(int, input().split())
    e,f = map(int, input().split())
    c = Counter([a,b,c,d,e,f])
    a = 0
    b = 0
    for i in c.values():
        if i==1:
            a+=1
        if i==2:
            b+=1
    if a==2 and b==2:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()