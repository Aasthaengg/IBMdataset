def solve():
    INF = float('inf')

    def Dijkstra(adjList, vSt):
        numV = len(adjList)
        useds = [False] * numV
        numUsed = 0
        costs = [INF] * numV
        costs[vSt] = 0
        while True:
            cNow, vNow = INF, -1
            for v in range(numV):
                if useds[v]: continue
                if costs[v] < cNow:
                    cNow, vNow = costs[v], v
            useds[vNow] = True
            numUsed += 1
            if numUsed == numV: break
            for v2, wt in adjList[vNow]:
                c2 = cNow + wt
                if c2 < costs[v2]:
                    costs[v2] = c2
        return costs

    N, M, L = map(int, input().split())
    adjL = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A, B = A-1, B-1
        adjL[A].append((B, C))
        adjL[B].append((A, C))

    costss = [Dijkstra(adjL, vSt) for vSt in range(N)]

    adjL2 = [[] for _ in range(N)]
    for i, costs in enumerate(costss):
        for j, cost in enumerate(costs[i+1:], i+1):
            if cost <= L:
                adjL2[i].append((j, 1))
                adjL2[j].append((i, 1))

    costss = [Dijkstra(adjL2, vSt) for vSt in range(N)]

    Q = int(input())
    anss = []
    for _ in range(Q):
        s, t = map(int, input().split())
        s, t = s-1, t-1
        if costss[s][t] == INF:
            anss.append(-1)
        else:
            anss.append(costss[s][t]-1)

    print('\n'.join(map(str, anss)))


solve()
