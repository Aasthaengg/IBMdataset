import sys
input=sys.stdin.readline

n,k=map(int,input().split())
h=list(map(int,input().split()))

dp=[None]*n
dp[0]=0
dp[1]=abs(h[1]-h[0])

for i in range(2,n):
    kouho=[]
    for j in range(1,k+1):
        if i-j>=0:
            kouho.append(dp[i-j]+abs(h[i-j]-h[i]))
    dp[i]=min(kouho)

print(dp[-1])