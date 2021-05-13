n = int(input())
l = []
dp = [[0 for i in range(3)]for j in range(n)]
for i in range(n):
    l.append(list(map(int , input().split())))
dp[0][0] = l[0][0]
dp[0][1] = l[0][1]
dp[0][2] = l[0][2]
for i in range(n-1):
    dp[i+1][0] = l[i+1][0]+max(dp[i][1],dp[i][2])
    dp[i+1][1] = l[i+1][1]+max(dp[i][0],dp[i][2])
    dp[i+1][2] = l[i+1][2]+max(dp[i][1],dp[i][0])
print(max(dp[-1]))