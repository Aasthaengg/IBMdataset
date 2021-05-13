N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [False]*(K+1) #if First loses, "false"
for num in range(K):
  if not(dp[num]):
    for stone in a:
      if num + stone <= K:
        dp[num+stone] = True
if dp[K]:
  print("First")
else:
  print("Second")


