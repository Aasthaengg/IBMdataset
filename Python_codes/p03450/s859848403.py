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

    inf = 10**17
    #mod = 10**9 + 7

    n,m = map(int, input().split())

    #[行先, 距離]
    adj = [[] for _ in range(n)] #頂点数, 場合によって変える
    for _ in range(m):
        l,r,d = map(int, input().split())
        adj[l-1].append([r-1, d])
        adj[r-1].append([l-1, -d])

    x = [inf]*n

    def bfs(v):
        if x[v]==inf:
            x[v] = 0
        d = deque([v])
        while d:
            v  = d.popleft()
            for nv, cost in adj[v]:
                if x[nv] == inf:
                    x[nv] = x[v] + cost
                    d.append(nv)
                else:
                    if x[nv] - x[v] != cost:
                        return False
        return True

    for v in range(n):
        if not bfs(v):
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()
