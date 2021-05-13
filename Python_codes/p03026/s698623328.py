import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
edges = [[]for _ in range(n)]
for _ in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    edges[a].append(b)
    edges[b].append(a)


cost = sorted(map(int, input().split()))
m = 0
ans = [None]*n


def dfs(v, parent):
    ans[v] = cost.pop()
    if parent != -1:
        global m
        m += min(ans[v], ans[parent])
    for v2 in edges[v]:
        if v2 == parent:
            continue
        dfs(v2, v)


dfs(0, -1)
print(m)
print(*ans)
