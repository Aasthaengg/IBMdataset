n=int(input())
l=[]
for i in range(n):
    lo=input().split()
    l.append((int(lo[0]),int(lo[1]),int(lo[2])))
dp=[[0 for i in range(3)]for i in range(n)]
dp[0][0]=l[0][0]
dp[0][1]=l[0][1]
dp[0][2]=l[0][2]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][1],dp[i-1][2])+l[i][0]
    dp[i][1]=max(dp[i-1][2],dp[i-1][0])+l[i][1]
    dp[i][2]=max(dp[i-1][0],dp[i-1][1])+l[i][2]
print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))
