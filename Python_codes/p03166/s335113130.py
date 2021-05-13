import sys
N, M = map(int, input().split())

sys.setrecursionlimit(10**9)

vertices = [[] for i in range(N+1)]
dp = [-1] * (N+1)

for _ in range(M):
    fro, to = map(int, input().split())
    vertices[fro].append(to)

def dfs(i):
    
    if dp[i] != -1:
        return dp[i]
    
    temp = 0
    for vertex in vertices[i]:
        temp = max(temp, dfs(vertex)+1)
        
    dp[i] = temp
    return temp

for i in range(1,N+1):
    dfs(i)
    
print(max(dp))