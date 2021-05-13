n,m = map(int,input().split())
dp = [-10**5]*(n+1)
dp[0] = 0
t = [0,2,5,5,4,5,6,3,7,6]
a = set(map(int,input().split()))
for i in range(2,n+1):
  for x in a:
    if i-t[x] >= 0 and dp[i] < dp[i-t[x]] + 1:
      dp[i] = dp[i-t[x]] + 1
a = list(a)
a.sort(reverse=True)
cur = ""
idx = n
while idx:
  for x in a:
    if idx - t[x] >= 0 and dp[idx] == dp[idx-t[x]] + 1:
      cur += str(x)
      idx -= t[x]
      break
print(cur)