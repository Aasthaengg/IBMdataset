N = int(input())
P = list(map(float, input().split()))
DP = [[0]*(N+1)for _ in range(N+1)]
DP[0][0] = 1
for i in range(1,N+1):
    for j in range(N+1):
        if i < j:
            DP[i][j] = 0
        else:
            DP[i][j] = P[i-1] * DP[i-1][j-1] + (1 - P[i-1]) * DP[i-1][j]
print(sum(DP[N][N//2 + 1:]))