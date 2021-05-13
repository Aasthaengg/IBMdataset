import sys
sys.setrecursionlimit(10**6)
n,m=map(int,input().split())
adj=[]
dp=[0 for i in range(0,n+1)]
def dfs(i,p,adj,dp):
    # print(i)
    # print(i,p)
    if dp[i]!=0:
        return dp[i]
    for j in (adj[i]):
        if j==p:
            continue 
        else:
            dfs(j,i,adj,dp)
            dp[i]=max(dp[i],1+dp[j])
    return dp[i]
    
for i in range(n+1):
    adj.append([])
for _ in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)

for i in range(1,n+1):
    if dp[i]==0:
        dfs(i,i,adj,dp)
# print(dp)
print(max(dp))