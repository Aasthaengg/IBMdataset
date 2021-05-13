n = int(input())

price = {1}
for i in range(1, 100):
    tmp = 6**i
    if tmp > 10**5:
        break
    price.add(tmp)

for i in range(1, 100):
    tmp = 9**i
    if tmp > 10**5:
        break
    price.add(tmp)

price = list(price)
price.sort(reverse=True)

INF = 1 << 60

dp = [INF] * 2 * 10**5
dp[0] = 0
dp[1] = 1

for i in range(n + 1):
    for p in price:
        dp[i + p] = min(dp[i] + 1, dp[i + p])

print(dp[n])