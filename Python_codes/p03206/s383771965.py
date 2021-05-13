#どっちで出すか注意, rstrip注意
#提出前に見返すこと！
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    mod = 10**9 + 7

    d = int(input())
    if d==25:
        print('Christmas')
    elif d==24:
        print('Christmas Eve')
    elif d==23:
        print('Christmas Eve Eve')
    else:
        print('Christmas Eve Eve Eve')

if __name__ == '__main__':
    main()