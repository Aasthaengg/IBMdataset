n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [0 for _ in range(k + 1)]
for i in range(1, k + 1):
    for j in a:
        if i >= j:
            if dp[i - j] == 0:
                dp[i] = 1
        if dp[i] == 1:
            break
print("First" if dp[k] else "Second")