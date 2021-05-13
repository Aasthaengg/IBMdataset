N = 10**6
n = int(input())

nine = [1, 9]
while True:
    t = nine[-1] * 9
    if t > N:
        break
    nine.append(t)

six = [1, 6]
while True:
    t = six[-1] * 6
    if t > N:
        break
    six.append(t)

dp = [N]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    # dp[i] = min(dp[i], dp[i-1]+1)
    for j in nine:
        if i-j < 0:
            break
        dp[i] = min(dp[i], dp[i-j]+1)
    for j in six:
        if i-j < 0:
            break
        dp[i] = min(dp[i], dp[i-j]+1)

print(dp[n])