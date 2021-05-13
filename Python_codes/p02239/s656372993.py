import sys
# sys.stdin = open('input.txt')
from collections import deque

def fillMatrix():
    for i in range(n):
        u, k, *v = map(int, input().split())
        for j in v:
            matrix[i][j-1] = 1

def bfs(s):
    status[s] = VISITING
    distance[s] = 0
    Q.append(s)
    while len(Q) > 0:
        u = Q.popleft()
        for v in range(n):
            if matrix[u][v] and status[v] == NOT_VISITED:
                status[v] = VISITING
                distance[v] = distance[u] + 1
                Q.append(v)
        status[u] = VISITED

n = int(input())
matrix = [[0]*n for i in range(n)]
INFTY = 1 << 21
distance = [INFTY] * n

NOT_VISITED = 0 # WHITE
VISITING = 1 # GRAY
VISITED = 2 # BLACK
status = [NOT_VISITED] * n
Q = deque()

fillMatrix()
bfs(0)

for i in range(n):
    ans = []
    ans.append(i+1)
    if distance[i] == INFTY:
        distance[i] = -1
    ans.append(distance[i])
    ans = map(str, ans)
    print(' '.join(ans))
