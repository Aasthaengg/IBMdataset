import sys
from heapq import heapify, heappop, heappush

def solve():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    Edge = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        Edge[u-1].append(v-1)
    S, T = map(int, input().split())
    S -= 1
    T -= 1
    DP = [[1000000000 for j in range(N)] for i in range(3)]
    q = []
    heapify(q)
    heappush(q, (0, S, 0)) #回数, 頂点, mod
    while q:
        nc, nn, nlevel = heappop(q)
        if DP[nlevel][nn] == 1000000000:
            DP[nlevel][nn] = nc
            for nextnode in Edge[nn]:
                if nlevel == 2: heappush(q, (nc + 1, nextnode, 0))
                else: heappush(q, (nc, nextnode, nlevel + 1))
    if DP[0][T] < 1000000000: print(DP[0][T])
    else: print(-1)

    return 0

if __name__ == "__main__":
    solve()