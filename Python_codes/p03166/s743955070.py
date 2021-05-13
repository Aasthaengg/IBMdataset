import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def longest_path(s):
    global dp
    if dp[s-1]<1:
        if edge[s]:
            dp[s-1]=max((longest_path(t)+1)for t in edge[s])
        else:
            dp[s-1]=0
    return dp[s-1]

N,M=map(int,input().split())
edge={}
for i in range(1,N+1):
    edge.setdefault(i,[])
for _ in range(M):
    x,y=map(int,input().split())
    edge[x].append(y)
dp=[0]*N
for i in range(1,N+1):
    if dp[i-1]==0:
        longest_path(i)

print(max(dp))