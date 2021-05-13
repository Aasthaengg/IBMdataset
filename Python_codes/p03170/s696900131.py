n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] * (k + 1)
for i in range(k):
    if dp[i] == 0:
        for ai in a:
            if i + ai > k:
                break
            dp[i+ai] = 1
print('First' if dp[k] else 'Second')