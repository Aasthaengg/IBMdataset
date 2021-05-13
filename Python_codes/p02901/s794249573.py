n, m = map(int, input().split())
l = pow(2, n)
inf = pow(10, 7)
pow2 = [pow(2, i) for i in range(n)]
dp = [[inf] * l for _ in range(m + 1)]
dp[0][0] = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    bit = 0
    for j in c:
        bit += pow2[j - 1]
    for j in range(l):
        k = j | bit
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        dp[i][k] = min(dp[i][k], dp[i - 1][j] + a)
print(dp[m][l - 1] if not dp[m][l - 1] == inf else -1)