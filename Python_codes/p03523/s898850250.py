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

    res = ["AKIHABARA","KIHABARA","AKIHBARA","AKIHABRA","AKIHABAR","KIHBARA","KIHABRA","KIHABAR","AKIHBRA","AKIHBAR","AKIHABR","KIHBRA","KIHABR","KIHBAR","AKIHBR","KIHBR"]
    s = input().rstrip()
    for i in res:
        if i == s:
            print('YES')
            break
    else:
        print('NO')


if __name__ == '__main__':
    main()