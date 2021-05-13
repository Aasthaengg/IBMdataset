import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    edge[x-1].append(y-1)
dp = [-1]*N

def calc(x):
    if dp[x]!=-1:
        return dp[x]
    if not len(edge[x]):
        dp[x] = 0
        return 0
    dp[x] = max([calc(i) for i in edge[x]])+1
    return dp[x]

ans = 0
for i in range(N):
    ans = max(ans, calc(i))
print(ans)