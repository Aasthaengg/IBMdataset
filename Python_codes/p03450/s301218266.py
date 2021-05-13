import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v, d):
    if visited[v] and X[v] != d:
        return False
    if visited[v] and X[v] == d:
        return True
    visited[v] = True
    X[v] = d
    for u, c in E[v]:
        if not dfs(u, d + c):
            return False
    return True

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    E[l].append((r, d))
    E[r].append((l, -d))
X = [None] * N
visited = [False] * N
for v in range(N):
    if not visited[v]:
        if not dfs(v, 0):
            print('No')
            exit()
print('Yes')
