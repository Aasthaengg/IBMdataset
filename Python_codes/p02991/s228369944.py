def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math

    inf = 10**17
    #mod = 10**9 + 7

    n,m = map(int, input().split())
    adj = [[] for _ in range(n)] #頂点数, 場合によって変える
    for _ in range(m):
        a,b = map(int, input().split())
        adj[a-1].append(b-1)
    s,t = map(int, input().split())
    s -= 1
    t -= 1

    d1 = [inf]*n
    d2 = [inf]*n
    d0 = [inf]*n
    d0[s] = 0
    d = deque([[s, 0]])
    while d:
        v, hosuu = d.popleft()
        hosuu += 1
        for nv in adj[v]:
            if hosuu%3==1 and d1[nv]>hosuu:
                d1[nv] = hosuu 
                d.append([nv, hosuu])
            if hosuu%3==2 and d2[nv]>hosuu:
                d2[nv] = hosuu
                d.append([nv, hosuu])
            if hosuu%3==0 and d0[nv]>hosuu:
                d0[nv] = hosuu
                d.append([nv, hosuu])
    if d0[t]==inf:
        print(-1)
    else:
        print(d0[t]//3)

if __name__ == '__main__':
    main()