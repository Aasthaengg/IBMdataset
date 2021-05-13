import sys
from collections import deque
n, k = [int(i) for i in sys.stdin.readline().split()]
ls = []
graph = {i:[] for i in range(n)}
for i in range(n-1):
    a, b = [int(i) for i in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    ls.append((a, b))
MOD = 10**9+7
root = 0
que = deque([root])
colors = [-1 for i in range(n)]
parent = [-1 for i in range(n)]
grandpa = [-1 for i in range(n)]
already = {root}
res = k
while len(que) > 0:
    cur = que.popleft()
    cnt = 0
    for _next in graph[cur]:
        if _next == parent[cur]:
            continue
        parent[_next] = cur
        grandpa[_next] = parent[cur]
        que.append(_next)
        if parent[cur] != -1:
            res = res * (k - cnt - 2) % MOD
        else:
            res = res * (k - cnt - 1) % MOD
        cnt += 1
print(res)