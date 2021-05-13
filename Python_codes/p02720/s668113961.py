K = int(input())

if K <= 10:
    print(K)
    exit()


dp = [[0]*10 for _ in range(10)]    # i の最大値は　3234566667の10桁よりi = 9
i = 0
flg = False

for k in range(10):
    dp[0][k] = 1

S = 8
while True:
    i += 1
    for k in range(10):
        if k==9:
            dp[i][k] = dp[i-1][k] + dp[i-1][k-1]
        elif k == 0:
            dp[i][k] = dp[i - 1][k + 1] + dp[i - 1][k]
        else:
            dp[i][k] = dp[i - 1][k + 1] + dp[i - 1][k] + dp[i - 1][k - 1]
        if k != 0:
            S += dp[i][k]
        if S >= K-1:
            flg = True
            break
    if flg:
        break
i_max, k_max = i, k
i_max -= 1
res = [k_max]
for i in range(i_max, -1, -1):
    for k in reversed(range(k_max-1,k_max+2)):
        if k > 9 or k < 0:
            continue
        if S - dp[i][k] >= K-1:
            S -= dp[i][k]
        else:
            break
    k_max = k
    res.append(k)

print(*res, sep="")
