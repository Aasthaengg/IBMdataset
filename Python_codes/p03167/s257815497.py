n = input().split()
r = int(n[0])
c = int(n[1])

a = []
MOD = 10**9+7

for i in range(r):
    x = input()
    y = []
    for char in x:
        if char == '.':
            y.append(1)
        else:
            y.append(0)
    a.append(y)

if a:
    dp = [[0 for i in range(c)] for j in range(r)]

    dp[0][0] = a[0][0]

    for i in range(1,r):
        dp[i][0] = dp[i-1][0] * a[i-1][0]

    for j in range(1,c):
        dp[0][j] = dp[0][j-1] * a[0][j-1]

    for i in range(1,r):
        for j in range(1,c):
            dp[i][j] = dp[i-1][j] * a[i-1][j] + dp[i][j-1] * a[i][j-1]

print((dp[r-1][c-1] * a[r-1][c-1])%MOD)