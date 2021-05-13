import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
#dp[v]: start from v maxpath
dp = [-1 for _ in range(N)]

gragh = [[] for _ in range(N)]
for _ in range(M):
    x,y = map(int, input().split())
    gragh[x-1].append(y-1)

#solve DAG and topological sort by memo recursive funciton
def f(v,G=gragh):
    if dp[v] != -1:
        return dp[v]
    ret = 0
    for u in G[v]:
        ret = max(ret, f(u) + 1)
    dp[v] = ret
    return ret
for v in range(N):
    dp[v] = f(v)
print(max(dp))