


n, k = list(map(int, input().split()))

a = list(map(int, input().split()))


dp = [0]*(k + 1)

for i in range(1, k + 1):
    for move in a:
        if i - move >= 0:
            if dp[i - move] == 0:
                dp[i] = 1


if dp[i] == 1:
    print("First")

else:
    print("Second")