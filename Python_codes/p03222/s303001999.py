base = 10 ** 9 + 7
h, w, k = map(int, input().split())
wc = [1] * 9

for i in range(2, 9):
    wc[i] = wc[i-1] + wc[i-2]

dp = [0] * (w+2)
dp[1] = 1
for i in range(h):
    tmp = [0] * (w+2)
    for j in range(1, w+1):
        tmp[j] = dp[j] * wc[j-1] * wc[w-j]
        if j > 1:
            tmp[j] += dp[j-1] * wc[j-2] * wc[w-j]
        if j < w:
            tmp[j] += dp[j+1] *wc[j-1] * wc[w-j-1]
        tmp[j] = tmp[j] % base
    dp = tmp
print(dp[k])