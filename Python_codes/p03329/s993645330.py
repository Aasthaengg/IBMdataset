n = int(input())

l = [1]
i = 1
while 6 ** i <= 100000:
    l.append(6 ** i)
    i += 1
i = 1
while 9 ** i <= 100000:
    l.append(9 ** i)
    i += 1
l.sort()

dp = [float('inf')] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    for v in l:
        if v > i:
            break
        dp[i] = min(dp[i], dp[i-v] + 1)

print(dp[n])