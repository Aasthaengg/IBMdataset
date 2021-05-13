import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

from collections import deque
def BFS(N, graph, start):
    d = [-1 for i in range(N)]
    Q = deque([])
    Q.append(start)
    d[start] = 0
    while Q:
        v = Q.popleft()
        for u in graph[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                Q.append(u)
    return d

N, M = (int(i) for i in input().split())
graph = [[] for i in range(3*N)]
for i in range(M):
    a, b = (int(i) for i in input().split())
    graph[3*(a-1)].append(3*(b-1) + 1)
    graph[3*(a-1) + 1].append(3*(b-1) + 2)
    graph[3*(a-1) + 2].append(3*(b-1))

S, T = (int(i) for i in input().split())
ans = BFS(3*N, graph, 3*(S-1))
print(ans[3*(T-1)]//3)