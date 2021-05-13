N = int(input())
a = [[int(i) for i in input().split()] for _ in range(N)]
dp = a[0]

for i in range(1,N) :
    a[i][0] += max(dp[1],dp[2])
    a[i][1] += max(dp[2],dp[0])
    a[i][2] += max(dp[0],dp[1])
    dp = a[i]
print(max(dp))