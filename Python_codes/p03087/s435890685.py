n, q = map(int, input().split())
s = list(input())
dp = [0]*(n+10)
for i in range(n):
  if i == 0:
    continue
  else:
    if s[i]=='C' and s[i-1]=='A':
      dp[i+1] = dp[i] + 1
    else:
      dp[i+1] = dp[i]
for i in range(q):
  l, r = map(int, input().split())
  if l == 1:
    print(dp[r])
  else:
    if s[l-1]=='C' and s[l-2]=='A':
      print(dp[r]-dp[l-1]-1)
    else:
      print(dp[r]-dp[l-1])