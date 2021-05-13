from sys import stdin

# Input data
#stdin = open("input", "r")

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [0] * (n + 1)
dp[2] = abs(arr[1] - arr[0])
for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + abs(arr[i - 1] - arr[i - 2]),
                dp[i - 2] + abs(arr[i - 1] - arr[i - 3]))
print(dp[n])
