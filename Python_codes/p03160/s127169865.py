n = int(input())
stair = list(map(int,input().split()))
dp = [0 for i in range(n)]
for i in range(1,n):
    if(i == 1):
        dp[i] = dp[i-1]+abs(stair[i]-stair[i-1])
    else:
        dp[i] = min(dp[i-1]+abs(stair[i]-stair[i-1]),dp[i-2]+abs(stair[i]-stair[i-2]))
    # print(dp[i])
print(dp[-1])