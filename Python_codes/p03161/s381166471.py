# coding: utf-8
# Your code here!
N,K=map(int,input().split())

H=list(map(int,input().split()))

dp=[10**9]*(N)
dp[0]=0

for i in range(N):
    for j in range(i+1,min(i+1+K,N)):
        dp[j]=min(dp[i]+abs(H[j]-H[i]),dp[j])

print(dp[-1])
