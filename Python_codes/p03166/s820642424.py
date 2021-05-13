import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
edges = [[]*n for _ in range(n)]
#DAGみたらDPを考える！

#メモ化再帰
visited = [False]*n
memo = [0]*n
def dp(v):
    if visited[v]:
        return memo[v]
    ret = 0
    for child in edges[v]:
        ret = max(ret, dp(child)+1)
    visited[v] = True
    memo[v] = ret
    return ret


for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)

ans = 0
for i in range(n):
    ans = max(ans, dp(i))
print(ans)
#print(memo)