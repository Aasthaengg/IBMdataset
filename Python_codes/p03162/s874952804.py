N = int(input())
a = []
b = []
c = []
for i in range(N):
    num = list(map(int, input().split(' ')))
    a.append(num[0])
    b.append(num[1])
    c.append(num[2])
dp = [[0,0,0] for i in range(N)]
dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]
for i in range(1, N):
    dp[i][0] = max(dp[i -1][1] + a[i], dp[i -1][2] + a[i])
    dp[i][1] = max(dp[i -1][0] + b[i], dp[i -1][2] + b[i])
    dp[i][2] = max(dp[i -1][0] + c[i], dp[i -1][1] + c[i])
ans = max(dp[N -1][0], dp[N -1][1], dp[N -1][2])
print(ans)