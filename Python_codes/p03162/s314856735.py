n=int(input())
a=[0]
b=[0]
c=[0]
for i in range(n):
    A,B,C=map(int, input().split())
    a.append(A)
    b.append(B)
    c.append(C)

dp=[[10**10,10**10,10**10] for i in range(n+1)]

dp[0][0]=0
dp[0][1]=0
dp[0][2]=0

dp[1][0]=a[1]
dp[1][1]=b[1]
dp[1][2]=c[1]

for i in range(2,n+1):
    dp[i][0]=max(dp[i-1][1]+a[i],dp[i-1][2]+a[i])
    dp[i][1]=max(dp[i-1][0]+b[i],dp[i-1][2]+b[i])
    dp[i][2]=max(dp[i-1][1]+c[i],dp[i-1][0]+c[i])

print(max(dp[n]))