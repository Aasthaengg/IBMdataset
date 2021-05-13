# 最低でもN-1本の辺があり, これらの辺は頂点間を結ぶ最短経路となっている
# つまり, 距離1の最短経路は少なくともN-1個ある
# また, 頂点のペアはNC2でN*(N-1)//2個ある
# よって, Kとしてあり得るのはK<=N*(N-1)//2-(N-1)=(N-1)*(N-2)//2である

# という風に上限が証明できるけど, グラフを書いてみると
# Kが最大となるのはスター型のときと分かる

# ここで詰んで終わった

# 任意のK組をどうやって作るか... と考えると難しい
# 上限が分かっているのでここから減らす方針で考える
# 真ん中の頂点以外は全てのペアが距離2となっているので
# このペアを辺で繋ぐことで(N-1)*(N-2)//2個から減らしていく

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

    n,k = map(int, input().split())
    pair = (n-1)*(n-2)//2
    res = []
    if pair < k:
        print(-1)
    else:
        for i in range(1, n-1):
            if pair == k:
                break
            for j in range(i+1, n):
                if pair == k:
                    break
                pair -= 1
                res.append([i, j])
        print(n-1+len(res))
        for i in range(1, n):
            print(i, n)
        for a, b in res:
            print(a, b)


if __name__ == '__main__':
    main()