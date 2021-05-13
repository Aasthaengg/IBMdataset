n, m = map(int, input().split())
a, b, c = [], [], []
for i in range(m):
    ai, bi = map(int, input().split())
    a.append(ai); b.append(bi)
    ci = list(map(int, input().split()))
    c.append(ci)

dp = [[10**9 for j in range(2**n)] for i in range(m)]
key = 0
for i in range(b[0]):
    key += 1<<(c[0][i]-1)
dp[0][key] = a[0]
dp[0][0] = 0

for i in range(1, m):
    ai, bi, ci = a[i], b[i], c[i]
    key = 0
    for j in range(bi):
        key += 1<<(ci[j]-1)
    for j in range(2**n):
        dp[i][j|key] = min(dp[i-1][j|key], dp[i-1][j]+ai, dp[i][j|key])
    for j in range(2**n):
        dp[i][j] = min(dp[i-1][j], dp[i][j])

if dp[m-1][2**n-1] == 10**9:
    print(-1)
else:
    print(dp[m-1][2**n-1])