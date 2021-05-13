N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
nums = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-10**18]*(N+1)
dp[0] = 0

for i in range(N):
    for Ai in A:
        if i+nums[Ai]<=N:
            dp[i+nums[Ai]] = max(dp[i+nums[Ai]], dp[i]+1)

ans = []
now = N

for i in range(dp[N]):
    for Ai in A:
        if now-nums[Ai]>=0 and dp[now-nums[Ai]]==dp[N]-i-1:
            now -= nums[Ai]
            ans.append(str(Ai))
            break

print(''.join(ans))