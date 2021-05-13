def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    x,y,z,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ab = []
    for i in a:
        for j in b:
            ab.append(i+j)
    ab.sort(reverse=1)
    ab = ab[:k]
    abc = []
    for i in ab:
        for j in c:
            abc.append(i+j)
    abc.sort(reverse=1)
    for i in range(k):
        print(abc[i])

if __name__ == '__main__':
    main()