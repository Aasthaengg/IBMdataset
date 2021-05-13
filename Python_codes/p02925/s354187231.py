import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
tdlist = lambda i, j, value=0: [[value] * j for _ in range(i)]

n = int(input())
m = n * (n-1) // 2
graph = [list() for _ in range(m)]
deg = [0] * m

to_id = tdlist(n, n)
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        to_id[i][j], to_id[j][i] = cnt, cnt
        cnt += 1

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n-2):
        v = to_id[i][a[j]-1]
        u = to_id[i][a[j+1]-1]
        graph[v].append(u)
        deg[u] += 1

q = deque(v for v in range(m) if deg[v] == 0)
cnt = 0
dp = [0] * m

while q:
    v = q.popleft()
    cnt += 1
    for u in graph[v]:
        deg[u] -= 1
        dp[u] = max(dp[u], dp[v] + 1)
        if deg[u] == 0:
            q.append(u)

print(-1 if cnt != m else max(dp)+1)
