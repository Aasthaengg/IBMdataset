# input
N, K = map(int, input().split())
a = list(map(int, input().split()))

# dp
dp = ["W"] * (K + 1)

for i in range(K):
  if dp[K - i] == "W":
    for j in range(N):
      if K - i - a[j] < 0:
        continue
      dp[K - i - a[j]] = "L"

if dp[0] == "W":
  print("Second")
else:
  print("First")

