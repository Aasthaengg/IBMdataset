N = int(input())
A = [int(input()) for i in range(N)]

dp = [0]*(N+1)

for i in range(N) :
    a = A[i]
    dp[a] = dp[a-1]+1

ans = N - max(dp)

print(ans)
