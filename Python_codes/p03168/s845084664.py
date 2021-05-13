from sys import stdin
n = int(stdin.readline())
p = list(map(float,stdin.readline().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n+1):
    for j in range(n+1):
        if i>j:
            continue
        dp[i][j] += (0 if i==0 or j==0 else dp[i-1][j-1]*p[j-1])
        dp[i][j] += (0 if j==0 else dp[i][j-1]*(1-p[j-1]))
x = (n+1)//2
ans = 0
while x != n+1:
    ans += dp[x][-1]
    x += 1
print(ans)