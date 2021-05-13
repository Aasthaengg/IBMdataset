def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    inf = 10**17
    #mod = 10**9 + 7

    n,m,p = map(int, input().split())
    edge = [[] for _ in range(m)]
    adj = [[] for _ in range(n)]
    for i in range(m):
        a,b,c = map(int, input().split())
        edge[i] = [a-1,b-1,-(c-p)]
        adj[b-1].append(a-1)

    visited = [0]*n
    visited[-1] = 1
    dq = deque([n-1])
    while dq:
        v = dq.popleft()
        for nv in adj[v]:
            if visited[nv] == 0:
                visited[nv] = 1
                dq.append(nv)
    
    def bellmanford(n, s, edge):
        inf = 10**17
        d = [inf] * n
        d[s] = 0
        for i in range(n):
            for a,b,c in edge:
                if d[a] != inf and d[b] > d[a]+c:
                    d[b] = d[a] + c
                    if i == n-1 and visited[b] == 1:
                        return -inf
        return -d[-1]

    res = bellmanford(n,0,edge)
    if res == -inf:
        print(-1)
    elif res < 0:
        print(0)
    else:
        print(res)

if __name__ == '__main__':
    main()