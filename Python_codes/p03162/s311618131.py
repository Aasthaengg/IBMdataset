N = int(input())
a = [0] * N
b = [0] * N
c = [0] * N
for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())

dp=[[0 for i in range(3)] for j in range(N)] 
dp[0][0]=a[0]
dp[0][1]=b[0]
dp[0][2]=c[0]

for i in range(1,N):    
    dp[i][0]=max(dp[i-1][1]+a[i],dp[i-1][2]+a[i])
    dp[i][1]=max(dp[i-1][0]+b[i],dp[i-1][2]+b[i])
    dp[i][2]=max(dp[i-1][0]+c[i],dp[i-1][1]+c[i])

print(max(dp[-1][0],dp[-1][1],dp[-1][2]))