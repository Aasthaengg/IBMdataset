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
    
    # u高橋, s青木
    n,u,s = map(int, input().split())
    adj = [[] for _ in range(n)] #頂点数, 場合によって変える
    for _ in range(n-1):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    ta = [-1]*n
    ao = [-1]*n

    d = deque([s-1])
    ao[s-1] = 0
    while d:
        v = d.popleft()
        for nv in adj[v]:
            if ao[nv] == -1:
                ao[nv] = ao[v] + 1
                d.append(nv)

    d = deque([u-1])
    ta[u-1] = 0
    while d:
        v = d.popleft()
        for nv in adj[v]:
            if ta[nv] == -1:
                ta[nv] = ta[v] + 1
                d.append(nv)

    res = 0
    for i in range(n):
        if ta[i] < ao[i]:
            res = max(res, ao[i]-1)
    print(res)

if __name__ == '__main__':
    main()