import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int,input().split())

edges = [[] for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    edges[y-1].append(x-1)
    
used = [0 for _ in range(N)]
dp = [0 for _ in range(N)]

def dfs(pos):
    if not edges[pos]:
        dp[pos] = 0
        return
    for n_pos in edges[pos]:
        if not used[n_pos]:
            dfs(n_pos)
        used[n_pos] = 1
        dp[pos] = max(dp[pos],dp[n_pos]+1)

    
for i in range(N):
    if used[i]:
        continue
    used[i] = True
    dfs(i)

print(max(dp))