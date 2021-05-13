N, M = map(int, input().split())
e = [0,2,5,5,4,5,6,3,7,6]
dp = [-1]*(N+8)
dp[0] = 0
A = list(map(int, input().split()))
for n in range(N):
    if dp[n] == -1: continue
    for a in A:
        dp[n+e[a]] = max(dp[n+e[a]], dp[n]*10+a)
print(dp[N])