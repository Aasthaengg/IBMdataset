import sys
import itertools
# import numpy as np
import time

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
start = time.time()

N = int(readline())
A = [[int(x) - 1 for x in row.split()] for row in readlines()]


ids = [[0 for j in range(1005)] for i in range(1005)]
V = 0
for i in range(N):
    for j in range(i, N):
        ids[i][j] = V
        V += 1

MAXV = 1005 * 1005 // 2

visited = [False for i in range(MAXV)]
calculated = [False for i in range(MAXV)]
dp = [0 for i in range(MAXV)]

def dfs(v):
    if visited[v]:
        if not calculated[v]:
            print(-1)
            exit()

        return dp[v]

    visited[v] = True
    dp[v] = 1
    for u in to[v]:
        dp[v] = max(dp[v], dfs(u) + 1)

    calculated[v] = True
    return dp[v]

to = [[] for i in range(MAXV)]
for i in range(N):
    for j in range(N - 1):
        a = i
        b = A[i][j]
        if a > b:
            a, b = b, a
        A[i][j] = ids[a][b]
    for j in range(N - 2):
        to[A[i][j + 1]].append(A[i][j])

ans = 0
for i in range(V):
    ans = max(ans, dfs(i))

print(ans)
elapsed_time = time.time() - start
# print(elapsed_time)