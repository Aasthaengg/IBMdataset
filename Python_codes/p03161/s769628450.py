import sys

data = sys.stdin.readlines()

n, k = list(map(int, data[0].split()))
h = list(map(int, data[1].split()))

dp = [-1] * n
dp[0] = 0

for i in range(1, min(n, k)):
    dp[i] = min([dp[j] + abs(h[i]-h[j]) for j in range(i)])

for i in range(k, n):
    dp[i] = min([dp[i-j] + abs(h[i]-h[i-j]) for j in range(1, k+1)])

print(dp[n-1])