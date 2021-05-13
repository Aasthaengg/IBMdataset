import sys
input = sys.stdin.readline

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

bin_k = format(k, 'b').zfill(50)

b = [0] * 50 # ビットごとの1の個数

for i in a:
    bin_i = format(i, 'b').zfill(50)
    for j in range(len(bin_i)):
        if bin_i[j] == "1":
            b[j] += 1

dp = [[0, 0] for _ in range(len(bin_k))]

if bin_k[0] == "0":
    dp[0][0] = b[0] * 2**(len(bin_k) - 1) # 0
else:
    dp[0][0] = (n - b[0]) * 2**(len(bin_k) - 1) # 1
    dp[0][1] = b[0] * 2**(len(bin_k) - 1) # 0

for i in range(1, len(bin_k)):
    if bin_k[i] == "0":
        dp[i][0] = dp[i - 1][0] + b[i] * 2**(len(bin_k) - (i + 1))
        if dp[i - 1][1] > 0:
            dp[i][1] = max(dp[i - 1][1] + b[i] * 2**(len(bin_k) - (i + 1)), dp[i - 1][1] + (n - b[i]) * 2**(len(bin_k) - (i + 1)))
    else:
        dp[i][0] = dp[i - 1][0] + (n - b[i]) * 2**(len(bin_i) - (i + 1))
        dp[i][1] = dp[i - 1][0] + b[i] * 2**(len(bin_k) - (i + 1))
        if dp[i - 1][1] > 0:
            dp[i][1] = max(dp[i][1], dp[i - 1][1] + (n - b[i]) * 2**(len(bin_i) - (i + 1)), dp[i - 1][1] + b[i] * 2**(len(bin_k) - (i + 1))) 

print(max(dp[-1][0], dp[-1][1]))