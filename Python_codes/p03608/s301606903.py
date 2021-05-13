import sys,queue,math,copy,itertools,bisect,collections
from heapq import *

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**8
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    _LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N,M,R = LI()
    r = _LI()
    root = [[] for _ in range(N)]
    for _ in range(M):
        a,b,c = LI()
        root[a-1].append((b-1,c))
        root[b-1].append((a-1,c))

    memo = [[0] * N for _ in range(N)]

    min_r = INF
    for x in itertools.permutations(r):
        it = 0
        s = x[0]
        for t in x[1:]:
            if memo[s][t]:
                it += memo[s][t]
            else:
                node = [INF] * N
                q = []
                heapify(q)
                heappush(q,(0,s))
                node[s] = 0
                while q:
                    l,u = heappop(q)
                    if l > node[u]: continue
                    for v,m in root[u]:
                        if node[v] > l + m:
                            node[v] = l + m
                            heappush(q,(l+m,v))
                memo[s][t] = node[t]
                memo[t][s] = node[t]
                it += node[t]
            s = t
        min_r = min(min_r,it)
    print(min_r)

if __name__ == '__main__':
    main()