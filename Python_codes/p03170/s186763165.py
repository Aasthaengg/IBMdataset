N, K = map(int, input().split())
a = [int(x) for x in input().split()]

dp = [''] * (K + 1)
dp[0] = 'Second'

for i in range(K+1):
    if dp[i] == '':
        dp[i] = 'Second'
        for j in a:
            if j > i:
                break
            if dp[i-j] == 'Second':
                dp[i] = 'First'
                break
    if dp[i] == 'Second':
        for j in a:
            if i + j > K:
                break
            dp[i+j] = 'First'

print(dp[K])