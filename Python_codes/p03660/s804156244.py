# unionfindで共通部分の数調べたらいけるかと思ったけど
# 共通部分の構造が重要だった...

# 知りたいのは0とn-1間のパス上における優劣
# →BFSで各頂点までの距離を調べると白黒どちらになるか分かる

# (おまけ)各頂点に付けた順位はその数字の手数以下で
# どちらかの色がつくことが確定している

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

    n = int(input())
    adj = [[] for _ in range(n)] #頂点数, 場合によって変える
    for _ in range(n-1):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    black = [-1] * n
    white = [-1] * n
    f = deque([0])
    black[0] = 0
    s = deque([n-1])
    white[-1] = 0

    def bfs(q, color):
        while q:
            v = q.popleft()
            for nv in adj[v]:
                if color[nv] < 0:
                    color[nv] = color[v] + 1
                    q.append(nv)

    bfs(f, black)
    bfs(s, white)
    cnt = 0
    for i in range(n):
        if black[i] <= white[i]:
            cnt += 1
    if cnt > n-cnt:
        print('Fennec')
    else:
        print('Snuke')



if __name__ == '__main__':
    main()