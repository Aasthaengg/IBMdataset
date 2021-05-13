from collections import deque
import sys
input = sys.stdin.readline

INF = float('inf')

def bfsMinCosts(adjList, vSt):
    numV = len(adjList)
    costs = [INF] * numV
    costs[vSt] = 0
    Q = deque([vSt])
    while Q:
        vNow = Q.popleft()
        cNow = costs[vNow]
        for v2 in adjList[vNow]:
            if costs[v2] == INF:
                costs[v2] = cNow + 1
                Q.append(v2)
    return costs

N, M = map(int, input().split())
adjL = [[] for _ in range(3*N)]
for _ in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    adjL[3*u+0].append(3*v+1)
    adjL[3*u+1].append(3*v+2)
    adjL[3*u+2].append(3*v+0)

S, T = map(int, input().split())
S, T = S-1, T-1

costs = bfsMinCosts(adjL, 3*S+0)

if costs[3*T+0] == INF:
    print(-1)
else:
    print(costs[3*T+0]//3)
