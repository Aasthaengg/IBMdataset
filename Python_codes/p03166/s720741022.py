#input
import sys
sys.setrecursionlimit(10**7)
N, M = map(int, input().split())
z = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    z[x-1].append(y-1)

#output
#便宜的にすべての点を-1しておく。
#dp[i]を頂点iから始まるpathで最長の長さとする。
#dp[i] = max(dp[v]+1)(vは頂点iから到達できる任意の頂点)

visited = [False] * N
memo = [0] * N

def dp(v):
    if visited[v]:
        return memo[v]
    else:
        res = 0
        for u in z[v]:
            res = max(res, dp(u)+1)
        memo[v] = res
        visited[v] = True
        return res
for i in range(N):
    dp(i)

print(max(memo))