n = int(input())
c = [int(input()) for _ in range(n)]
mod = 10 ** 9 + 7
MAX = 2 * 10 ** 5

cc = []
prev = 0
for e in c:
    if e != prev:
        cc.append(e)
        prev = e

ln = len(cc)

dp = [0] * (ln + 1)
dp[0] = 1
acc = [0] * (MAX + 1)

for i, e in enumerate(cc, 1):
    dp[i] = dp[i-1] + acc[e]
    dp[i] %= mod

    acc[e] += dp[i-1]
    acc[e] %= mod

print(dp[ln])
