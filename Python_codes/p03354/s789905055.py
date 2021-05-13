import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n, m = map(int, input().split())
P = [int(p) - 1 for p in input().split()]

GRAPH = [[] for _ in range(n)]
for _ in range(m):
    x, y = [int(xy) - 1 for xy in input().split()]
    GRAPH[x].append(y); GRAPH[y].append(x)

def dfs(now):
    searched[now] = True
    p = P[now]
    A[now] = B[p] = color
    for next in GRAPH[now]:
        if searched[next]:
            continue
        dfs(next)

A = [0] * n; B = [0] * n
searched = [False] * n
color = 1
for i in range(n):
    if searched[i]:
        continue
    dfs(i)
    color += 1

ans = sum(A[i] == B[i] for i in range(n))

print(ans)
