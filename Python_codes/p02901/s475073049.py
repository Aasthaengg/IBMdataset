N, M = map(int, input().split())

dp = [[10**10 for B in range(1 << N)] for i in range(M+1)]
dp[0][0] = 0

for i in range(M):
    a, b = map(int, input().split())
    c = [int(j) for j in input().split()]
    C = sum([1 << (x-1) for x in c])

    for B in range(1 << N):
        dp[i+1][B] = min(dp[i][B], dp[i+1][B])
        dp[i+1][B | C] = min(dp[i+1][B | C], dp[i][B]+a)

if dp[M][(1 << N)-1] == 10**10:
    print(-1)
else:
    print(dp[M][(1 << N)-1])
