n = int(input())

sixs = [6]
while sixs[-1] * 6 <= n:
    sixs.append(sixs[-1] * 6)

nines = [9]
while nines[-1] * 9 <= n:
    nines.append(nines[-1] * 9)

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    dp[i] = dp[i-1] + 1
    for six in sixs:
        if i - six >= 0:
            dp[i] = min(dp[i], dp[i-six] + 1)

    for nine in nines:
        if i - nine >= 0:
            dp[i] = min(dp[i], dp[i-nine] + 1)

print(dp[-1])
