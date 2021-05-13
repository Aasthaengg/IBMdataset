n = int(input())
P = list(map(float, input().split()))

memo = [[0] * (2 * n + 1) for _ in range(n+1)]
memo[0][n] = 1
for i in range(1, n+1):
    p = P[i-1]
    for j in range(2 * n + 1):
        if j == 0:
            memo[i][j] = (1-p) * memo[i-1][j+1]
        elif j == 2 * n:
            memo[i][j] = p * memo[i-1][j-1]
        else:
            memo[i][j] = p * memo[i-1][j-1] + (1-p) * memo[i-1][j+1]
ans = 0
for i in range(n+1, 2*n + 1):
    ans += memo[-1][i]
print(ans)