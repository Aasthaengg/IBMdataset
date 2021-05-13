import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from collections import deque
def resolve():
    m, n = map(int, input().split())
    grid = [input() for _ in range(m)]

    Q = deque()
    dist = [[INF] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#':
                dist[i][j] = 0
                Q.append((i, j))

    D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while Q:
        i, j = Q.popleft()
        for di, dj in D:
            ni, nj = i + di, j + dj
            if not (0 <= ni < m and 0 <= nj < n):
                continue
            if dist[ni][nj] != INF:
                continue
            dist[ni][nj] = dist[i][j] + 1
            Q.append((ni, nj))


    print(max(dist[i][j] for i in range(m) for j in range(n)))
resolve()