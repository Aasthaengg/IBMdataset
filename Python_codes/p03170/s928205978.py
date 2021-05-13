n,k = map(int,input().split())
a = list(map(int,input().split()))
dp = [0]*(k+1)
for i in range(1,k+1):
  flg = 0
  for j in a:
    if i-j>=0:
      flg |= 1-dp[i-j]
  dp[i] = flg
if dp[k]:
  print("First")
else:
  print("Second")