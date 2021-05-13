n = int(input())
dp = [0, 0, 0] # last activity was A/B/C
for _ in range(n):
    ndp = [0] * 3
    d = list(map(int, input().split()))
    for i in range(3):
        ndp[i] = d[i] + max(dp[j] for j in range(3) if j != i)
    dp = ndp
print(max(dp))