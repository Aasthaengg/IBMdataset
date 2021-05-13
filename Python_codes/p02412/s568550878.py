def countCombinations(n, x, size=3):
    dp = [[0 for j in range(x + 1)] for i in range(size + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for row in range(size - 1, -1, -1):
            for col in range(x + 1 - i):
                dp[1+row][i+col] += dp[row][col]
    return dp[-1][-1]



while True:
    m, n = (int(x) for x in input().split())
    if m==0 and n==0:
        quit()
    ans = countCombinations(m, n)
    print(ans)
