n,m=map(int,input().split())

A=list(map(int,input().split()))

N=[0,2,5,5,4,5,6,3,7,6]
X=[]
dp=[0]+[-1]*n*9

for i in range(n):
    for j in A:
        if dp[i]>=0:
            dp[i+N[j]]=max(dp[i+N[j]],dp[i]*10+j)

print(dp[n])