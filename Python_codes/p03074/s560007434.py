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
    N,K = map(int, input().split())
    s = list(input().rstrip())
    l = []
    for k,v in groupby(s):
        l.append(len(list(v)))

    res = 0
    if s[0]=='1':
        start = 0
        stop = 2*K+1
        res = sum(l[:stop])
        ans = res
        while start<len(l):
            res += sum(l[stop:stop+2])-sum(l[start:start+2])
            ans = max(ans, res)
            start += 2
            stop += 2
    else:
        start = 1
        stop = 2*K+2
        res = sum(l[start:stop])
        ans = res
        while start<len(l):
            res += sum(l[stop:stop+2])-sum(l[start:start+2])
            ans = max(ans, res)
            start += 2
            stop += 2
        ans = max(ans, sum(l[:2*K]))
    print(ans)

if __name__ == '__main__':
    main()