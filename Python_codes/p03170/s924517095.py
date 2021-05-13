n, k = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (k + 1)
dp[0] = 0
for i in range(k + 1):
    for j in arr:
        if i >= j and not dp[i - j]:
            dp[i] = 1
print("First" if dp[-1] else "Second")
