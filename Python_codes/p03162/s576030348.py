n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))

nums = [0,1,2]
dp = [[0]*3 for _ in range(n)]

# print(dp)
dp[0] = l[0]

for i in range(1,n):
    for jnow in range(3):
        for jpre in nums:
            if jpre != jnow:
                dp[i][jnow] = max(dp[i][jnow],dp[i-1][jpre]+l[i][jnow])
print(max(dp[n-1]))