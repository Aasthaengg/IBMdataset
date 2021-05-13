N, M = map(int, input().split())

dp = [10**10 for B in range(1 << N)]
dp[0] = 0

for i in range(M):
    a, b = map(int, input().split())
    c = [int(j) for j in input().split()]
    C = sum([1 << (x-1) for x in c])

    for B in range(1 << N):
        dp[B | C] = min(dp[B | C], dp[B]+a)

if dp[(1 << N)-1] == 10**10:
    print(-1)
else:
    print(dp[(1 << N)-1])
