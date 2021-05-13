n= int(input())
x=[]
for i in  range(n):
    x.append([int(x ) for  x in input().split()])

dp = [[x[0][0],x[0][1],x[0][2]] for i in range(n)]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][1],dp[i-1][2])+x[i][0]
    dp[i][1]=max(dp[i-1][0],dp[i-1][2])+x[i][1]
    dp[i][2]=max(dp[i-1][1],dp[i-1][0])+x[i][2]
print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))