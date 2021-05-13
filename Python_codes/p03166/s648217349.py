# BFS的にやるDAGの最長経路
from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

g = [[] for _ in range(n)]
indeg = [0 for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    # 入力を持つ点から始めても最長辺は作れない
    indeg[y-1] += 1

dp = [0 for _ in range(n)]
q = deque([])

# 最長辺の候補を入れる
for i in range(n):
    if indeg[i] == 0:
        q.append(i)

while q:
    v = q.popleft()
    for w in g[v]:
        indeg[w] -= 1
        if indeg[w] == 0:
            q.append(w)
            dp[w] = max(dp[w], dp[v] + 1)

print(max(dp))
