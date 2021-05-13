def calc(num):
    a, b, c = 0, 0, 0
    for i in range(2 ** (w - 1)):
        kk = 0
        kkk = 0
        t = "0" * (w - 1 - len(bin(i)[2:])) + bin(i)[2:]
        if ("11" not in t):
            if (num <= w - 2):
                if (t[num] == "1"):
                    c += 1
                    kk = 1
            if (num - 1 >= 0):
                if (t[num - 1] == "1"):
                    b += 1
                    kkk = 1
            if (kk + kkk) == 0:
                a += 1
    return a, b, c


h, w, k = map(int, input().split())
k -= 1
mod = (10 ** 9) + 7
dp = [[0 for _ in range(w)] for _ in range(h + 1)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        a, b, c = calc(j)
        dp[i + 1][j] = ((dp[i][j] * a) + dp[i + 1][j]) % mod
        if j - 1 >= 0:
            dp[i + 1][j - 1] = ((dp[i][j] * b) + dp[i + 1][j - 1]) % mod
        if j + 1 < w:
            dp[i + 1][j + 1] = ((dp[i][j] * c) + dp[i + 1][j + 1]) % mod
print(dp[h][k])