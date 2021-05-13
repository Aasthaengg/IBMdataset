n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

dp = [0 for i in range(k+1)]

for i in range(len(dp)):
    if dp[i] == 0:
        for j in arr:
            if j+i < k+1:
                dp[j+i] = 1

ans = "First" if dp[-1] else "Second"
print(ans)