N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = ['First']*(K+1)
dp[0] = 'Second'
def solve(dp):
    for i in range(1,K+1):
        for j in range(N):
            dp[i] = 'Second'
            if dp[i-A[j]]=='Second':
                dp[i] = 'First'
                break
    ans = dp[K]
    return ans
print(solve(dp))