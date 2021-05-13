amari = [i for i in range(10)]
p = 10**9 + 7
s =  str(input())
n = len(s)
ans = [0]*13
ans[0] = 1
for i in reversed(s):
  dp = [0]*13
  if i == '?':
    for j in range(13):
      for k in amari:
        dp[(j + k)%13] += ans[j]
  else:
    for j in range(13):
      dp[(j + amari[int(i)])%13] += ans[j]
      
  for i in range(len(dp)):
    dp[i] %= p
  ans = dp
  for i in range(len(amari)):
    amari[i] = amari[i]*10%13
print(ans[5])