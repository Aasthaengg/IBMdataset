from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)


def dfs(prev, u):
    if visited[u]:
        return
    else:
        cnt[u] += cnt[prev]
        visited[u] = True
        for nu in graph[u]:
            if visited[nu]:
                continue
            else:
                dfs(u, nu)


n, q = map(int, input().split())
graph = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = [0] * (n + 1)

for _ in range(q):
    p, x = map(int, input().split())
    cnt[p] += x

visited = [False] * (n + 1)

dfs(0, 1)

print(*cnt[1:])