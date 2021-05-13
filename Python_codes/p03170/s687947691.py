n, k = map(int, input().split())
A = list(map(int, input().split()))
dp = [0]*(k+1)
for i in range(1, k+1):
    for j in range(n):
        if i-A[j] < 0:
            continue
        dp[i] |= not dp[i-A[j]]
print('First' if dp[k] else 'Second')