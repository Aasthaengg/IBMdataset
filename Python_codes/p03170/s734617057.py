N, K = map(int, input().split())
a = list(map(int, input().split()))

dp = [-1] * (K+1)
dp[0] = 1
for i in range(1, K+1):
    l = [dp[i-aj] if i-aj>=0 else 0 for aj in a]
    dp[i] = 0 if 1 in l else 1
        
ans = 'First' if dp[-1] == 0 else 'Second'
print(ans)