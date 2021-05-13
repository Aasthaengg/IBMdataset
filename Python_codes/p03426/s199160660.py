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

    h,w,d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    zahyou = [[] for _ in range(d)]
    for x in range(h):
        for y in range(w):
            b = a[x][y] % d
            zahyou[b].append([a[x][y], x, y])

    mp = [[] for _ in range(d)]
    for i in range(d):
        xy = zahyou[i]
        xy.sort()
        mp[i].append(0)
        cx, cy = xy[0][1:]
        for j in range(1, len(xy)):
            mp[i].append(abs(xy[j][1]-cx)+abs(xy[j][2]-cy))
            cx, cy = xy[j][1:]
        mp[i] = list(accumulate(mp[i]))
    
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        amari = l % d
        l = (l-1) // d
        r = (r-1) // d
        print(mp[amari][r] - mp[amari][l])

if __name__ == '__main__':
    main()