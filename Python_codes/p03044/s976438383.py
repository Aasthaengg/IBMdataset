import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, input().split())
    edges[u-1].append((w, v-1))
    edges[v-1].append((w, u-1))


color = [-1]*n


def dfs(v, d, parent):
    color[v] = d & 1
    for d2, v2 in edges[v]:
        if v2 == parent:
            continue
        dfs(v2, d+d2, v)


dfs(0, 0, -1)
print(*color, sep='\n')