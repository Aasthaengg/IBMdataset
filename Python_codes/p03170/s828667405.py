n, k  = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * (k + 1)

for i in range(1, k + 1):
  if all(dp[i - a] == 1 for a in A if i >= a):
    dp[i] = 0
  else:
    dp[i] = 1

print("First" if dp[k] == 1 else "Second")