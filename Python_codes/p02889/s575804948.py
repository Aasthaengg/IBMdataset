import sys
input = sys.stdin.readline

def solve():
    INF = float('inf')

    def WarshallFloyd(adjList, INF):
        numV = len(adjList)
        D = [[INF]*numV for _ in range(numV)]
        for u, adj in enumerate(adjList):
            for v, wt in adj:
                D[u][v] = wt
            D[u][u] = 0

        for k in range(numV):
            Dk = D[k]
            for i in range(numV):
                Di = D[i]
                Dik = Di[k]
                for j in range(numV):
                    D2 = Dik + Dk[j]
                    if D2 < Di[j]:
                        D[i][j] = D2

        return D

    N, M, L = map(int, input().split())
    adjL = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1
        adjL[a].append((b, c))
        adjL[b].append((a, c))
    Q = int(input())
    querys = [tuple(map(int, input().split())) for _ in range(Q)]

    cost1ss = WarshallFloyd(adjL, INF)

    adjL2 = [[] for _ in range(N)]
    for a in range(N):
        for b in range(a+1, N):
            if cost1ss[a][b] <= L:
                adjL2[a].append((b, 1))
                adjL2[b].append((a, 1))

    cost2ss = WarshallFloyd(adjL2, INF)

    anss = []
    for s, t in querys:
        s, t = s-1, t-1
        cost = cost2ss[s][t]
        if cost == INF:
            anss.append(-1)
        else:
            anss.append(cost-1)

    print('\n'.join(map(str, anss)))


solve()
