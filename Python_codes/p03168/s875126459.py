# coding: utf-8
# Your code here!
N=int(input())

P=list(map(float,input().split()))

dp=[[0 for i in range(N+1)] for j in range(N+1)]
dp[0][0]=1

for i in range(N):
    for j in range(N-i):
        dp[i+1][j]+=dp[i][j]*P[i+j]
        dp[i][j+1]+=dp[i][j]*(1-P[i+j])        

ans=0
start=(N+1)//2
j=0
for i in range(start,N+1)[::-1]:
    ans+=dp[i][j]
    j+=1
print(ans)
#print(dp)


