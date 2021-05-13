import sys
input = sys.stdin.readline
from collections import deque
N = int(input())

X = [[] for i in range(N)]
for i in range(N-1):
    x, y = map(int, input().split())
    X[x-1].append(y-1)
    X[y-1].append(x-1)

def BFS(n, E, i0):
    Q = deque([i0])
    D = [-1] * n
    D[i0] = 0
    while Q:
        x = Q.popleft()
        for c in E[x]:
            if D[c] == -1:
                D[c] = D[x] + 1
                Q.append(c)
    return D

A = BFS(N, X, 0)
B = BFS(N, X, N-1)
print("Snuke" if sum([A[i] <= B[i] for i in range(N)]) * 2 <= N else "Fennec")