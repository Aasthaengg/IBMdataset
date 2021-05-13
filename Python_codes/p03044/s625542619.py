import sys
sys.setrecursionlimit(10**7)
n = int(input())
to = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    to[u].append((v, w))
    to[v].append((u, w))
ans = [-1] * n
def dfs(u=0, c=0, parent=-1):
    ans[u] = c
    for v, w in to[u]:
        if v == parent:
            continue
        dfs(v, (c + w) & 1, u)

dfs()
print(*ans, sep='\n')
