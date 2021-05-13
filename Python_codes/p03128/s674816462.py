n, m = map(int, input().split())
A = list(map(int, input().split()))
digit = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

dp = [(-1, -1)]*(n+1)
dp[0] = (0, -1)
for k in range(1, n+1):
    max_value = -1
    max_d = -1
    for num in A:
        if k >= digit[num]:
            suf, d = dp[k - digit[num]]
            if suf >= 0:
                value = num * (10 ** (d + 1)) + suf
                if value > max_value:
                    max_value = value
                    max_d = d + 1

    dp[k] = (max_value, max_d)
print(dp[n][0])