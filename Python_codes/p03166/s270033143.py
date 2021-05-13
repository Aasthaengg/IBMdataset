import sys
sys.setrecursionlimit(110000) #再帰上限はデフォルトで1000回までなので，増やす。

N, M = map(int, input().split())

graph = [[] for _ in range(110000)]

for _ in range(M):
    x, y = map(int, input().split())

    graph[x].append(y)

dp_memo = [-1] * 110000

def dp(v):
    if dp_memo[v] != -1:
        return dp_memo[v]

    ret = 0
    for item in graph[v]:
        ret = max(ret, dp(item) + 1)

    dp_memo[v] = ret
    return ret

ans = 0

for i in range(1, N+1):
    ans = max(ans, dp(i))

print(ans)