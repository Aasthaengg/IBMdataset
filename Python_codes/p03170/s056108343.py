n, k = map(int, input().split())
arr = [int(x) for x in input().split()]

dp = [False] * (k+1)

for stones in range(k+1):
    for num in arr:
        # If i'm choosing num stones and dp[stones - num] is false then opponent will loose
        if stones >= num and not dp[stones-num]:
            dp[stones] = True

ans = "First" if dp[k] else "Second"
print(ans)