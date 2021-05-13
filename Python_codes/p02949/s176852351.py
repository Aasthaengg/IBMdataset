from collections import deque
import sys
input = sys.stdin.readline

INF = float('inf')

def BellmanFord(adjList, vSt, INF):
    numV = len(adjList)
    negINF = -INF
    costs = [INF] * numV
    costs[vSt] = 0
    vNows = set([vSt])

    for _ in range(numV):
        vChangeds = set()
        for vFr in vNows:
            costFr = costs[vFr]
            for vTo, wt in adjList[vFr]:
                c2 = costFr + wt
                if c2 < costs[vTo]:
                    costs[vTo] = c2
                    vChangeds.add(vTo)
        if not vChangeds:
            return costs
        vNows = vChangeds

    for v in vNows:
        costs[v] = negINF

    Q = deque(vNows)
    while Q:
        vFr = Q.popleft()
        for vTo, wt in adjList[vFr]:
            if costs[vTo] == negINF: continue
            costs[vTo] = negINF
            Q.append(vTo)

    return costs


N, M, P = map(int, input().split())
adjL = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    A, B = A-1, B-1
    adjL[A].append((B, -C+P))

costs = BellmanFord(adjL, 0, INF)

ans = costs[N-1]
if ans == -INF:
    print(-1)
else:
    print(max(0, -ans))
