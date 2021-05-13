from sys import stdin
N,K=map(int,stdin.readline().split())
h=[int(i) for i in stdin.readline().split()][:N]
dp=[float('inf') for i in range(N)]
dp[0]=0
for i in range(N):
    for j in range(i+1,i+K+1):
        if j<N:
            dp[j]=min(dp[j],dp[i]+abs(h[j]-h[i]))
    #print(dp)
print(dp[-1])