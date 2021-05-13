N = int(input())
A = list(map(int,(input().split())))
B = [(0)*2 for _ in range(N)]
for i in range(N):
    B[i] = (A[i],i)
B.sort(reverse=True)

dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 0

ans = []
for l in range(N+1):
    for r in range(N+1):
        if l+r == N:
            ans.append(dp[l][r])
            break
        if r+1 < N+1:
            dp[l][r+1] = max(dp[l][r+1], dp[l][r] + B[l+r][0] * abs(B[l+r][1] - (N-(r+1)) ))
        if l+1 < N+1:
            dp[l+1][r] = max(dp[l+1][r], dp[l][r] + B[l+r][0] * abs(B[l+r][1] - l))

print(max(ans))