def resolve():
    x = int(input())
    dp = [0] * (x+1+105)
    dp[0] = 1

    for i in range(x):
        if dp[i] == 1:
            for j in range(100, 106):
                dp[i+j] = 1
    print(dp[x])
resolve()