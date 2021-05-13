X = int(input())

dp = [0] * (100200)
dp[0] = 1

for i in range(X + 1):
    if dp[i] == 1:
        for j in range(6):
            dp[i + 100 + j] = 1
            if i + 100 + j == X:
                print(1)
                exit()
print(0)
