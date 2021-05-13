#pypyは内包表記使わない, rstrip注意
#提出前に見返すこと！
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 1000000007

    s = input().rstrip()
    K = int(input())
    a = sorted(set(s))
    res = set()
    n = len(s)
    for i in a:
        res.add(i)
        if len(res)>=K:
            res = sorted(res)
            print(res[K-1])
            exit()
        for j in range(n):
            if s[j] == i:
                for k in range(1, 5):
                    res.add(s[j:j+k+1])
        if len(res)>=K:
            res = sorted(res)
            print(res[K-1])
            exit()



if __name__ == '__main__':
    main()