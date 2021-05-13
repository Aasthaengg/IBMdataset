def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n,a,b,c = map(int, input().split())
    l = [int(input()) for _ in range(n)]


    res = 10**20
    #各竹について0~3で場合分け
    for s in range(1<<(2*n)):
        l1 = []
        l2 = []
        l3 = []
        mp = 0
        #iセット目(i本目)
        for i in range(0, 2*n, 2):
            num = (s>>i) & 1 + ((s>>(i+1)) & 1)*2
            if num==1:
                l1.append(l[i//2])
            elif num==2:
                l2.append(l[i//2])
            elif num==3:
                l3.append(l[i//2])
        d, e, f = len(l1), len(l2), len(l3)
        if d==0 or e==0 or f==0:
            continue
        mp += (d+e+f-3)*10
        mp += abs(sum(l1)-a) + abs(sum(l2)-b) + abs(sum(l3)-c)
        res = min(res, mp)
    print(res)

if __name__ == '__main__':
    main()