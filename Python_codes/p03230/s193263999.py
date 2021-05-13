n = int(input())
i = 1
m = 0
while True:
    m += i
    if m == n:
        k = i + 1
        c = 1
        break
    elif m > n:
        c = 0
        break
    i += 1
if c == 1:
    print("Yes")
    print(k)
    dp = [[0 for _ in range(k - 1)] for _ in range(k)]
    m = 0
    for i in range(k):
        for j in range(k - 1):
            if i <= j:
                m += 1
                dp[i][j] = m
            else:
                if i == j + 1:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + 1
    for i in range(k):
        print(k - 1, end = " ")
        s = map(str, dp[i])
        print(" ".join(s))
else:
    print("No")