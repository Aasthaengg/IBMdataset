n, k = map(int, input().split())
a = list(map(int, input().split()))

digit_n = 0
kk = k
while kk > 0:
    kk >>= 1
    digit_n += 1

count = [0] * digit_n
mask = ~((1 << digit_n) - 1)

ans = 0
for i in range(n):
    ans += a[i] & mask
    for j in range(digit_n):
        if (a[i] >> j) & 1:
            count[j] += 1 

dp = [[0] * (digit_n + 1) for _ in range(2)]

for i in range(1, digit_n + 1):
    j = digit_n - i
    bit = (k >> j) & 1
    dp[0][i] = (dp[0][i-1] << 1) + (n - count[j] if bit else count[j])
    if dp[1][i-1]:
        dp[1][i] = (dp[1][i-1] << 1) + max(n - count[j], count[j])
    if bit == 1:
        dp[1][i] = max(dp[1][i], (dp[0][i-1] << 1) + count[j])
ans += max(dp[0][-1], dp[1][-1])
print(ans)