import sys

sys.setrecursionlimit(100000)

def rec(v):
    global dp, path
    if dp[v] != -1:
        return dp[v]

    res = 0
    for i in path[v]:
        res = max(res, rec(i)+1)

    dp[v] = res
    return res



N, M = map(int, input().strip().split(" "))

dp = [-1] * N
path = [[] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().strip().split(" "))
    path[x-1].append(y-1)


result = 0
for i in range(N):
    result = max(result, rec(i))

print(result)