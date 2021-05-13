import sys,queue,math,copy,itertools,bisect,collections
from heapq import *

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**5
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()
    root = [[] for _ in range(N)]
    for i in range(M):
        a,b,c = LI()
        root[a-1].append((b-1,c,i))
        root[b-1].append((a-1,c,i))

    rest = [1] * M
    q = []
    heapify(q)

    for i in range(N):
        node = [INF] * N
        heappush(q,(0,i,-1))
        while q:
            d,v,m = heappop(q)
            if node[v] < d: continue
            if m >= 0: rest[m] = 0
            for u,c,n in root[v]:
                if d + c < node[u]:
                    node[u] = d + c
                    heappush(q,(d+c,u,n))
    print(sum(rest))




if __name__ == '__main__':
    main()