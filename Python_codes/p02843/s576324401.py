X = int(input())
num = [105, 104, 103, 102, 101, 100]

dp = [0 for _ in range(X+1)]
dp[0] = 1
f = 1

for i in range(X+1):
    for j in num:
        if i-j >= 0:
            if dp[i-j]:
                dp[i] = 1

print(dp[X])