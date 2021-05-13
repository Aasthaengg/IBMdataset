N = int(input())
Dp = [a for a in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1,7):
        if i >= (6 ** j):
            Dp[i] = min(Dp[i], Dp[i-6**j] + 1)
    for h in range(1,6):
        if i >= (9 ** h):
            Dp[i] = min(Dp[i], Dp[i-9**h] + 1)
print(Dp[N])    