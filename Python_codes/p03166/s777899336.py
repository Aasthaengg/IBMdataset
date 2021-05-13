import sys
from collections import defaultdict
    
sys.setrecursionlimit(10**9)
    
n, m = map(int, input().split())
adj = defaultdict(list)
radj = defaultdict(list)

for i in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    
dp = [-1]*(n+1)

def dfs(e):
    if dp[e] != -1:
        return dp[e]
    
    temp = 0
    for i in adj[e]:
        temp = max(temp, 1+dfs(i))
        
    dp[e] = temp
    return temp
    
    
for i in range(1, n+1):
    dfs(i)
    
print(max(dp))