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

    N,C = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    # 各余りのマスのグループをi番目の色に変えた時の違和感の総和
    iwakan = [[0]*C for _ in range(3)]

    for i in range(N):
        for j in range(N):
            amari = (i+j+2) % 3
            color = c[i][j]
            for k in range(C):
                iwakan[amari][k] += d[color-1][k]
    
    res = 10**20
    for i in permutations(range(C), 3):
        res = min(res, iwakan[0][i[0]]+iwakan[1][i[1]]+iwakan[2][i[2]])
    print(res)

if __name__ == '__main__':
    main()