import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
links = [[] for _ in range(N+1)]
for _ in range(M):
    s, t = map(int, input().split())
    links[s].append(t)

dp = [-1 for _ in range(N+1)]
def search(i):
    if dp[i] != -1:
        return dp[i]
    
    paths = 0
    for t in links[i]:
        paths = max(paths, search(t)+1)
    
    dp[i] = paths
    return paths

for i in range(1, N+1):
    search(i)

print(max(dp))