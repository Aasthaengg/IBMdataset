n = int(input())
cc = [int(input()) for i in range(n)]
c = [cc[0]]
for i in range(1,n):
  if cc[i] != cc[i-1]:
    c.append(cc[i])

n = len(c)
dp = [0 for i in range(n)]
pos_dp = [-1 for i in range(2*10**5+1)]

dp[0] = 1
pos_dp[c[0]] = 0
     
for i in range(1,n):
  if pos_dp[c[i]]!=-1:
    dp[i] = (dp[i-1] + dp[pos_dp[c[i]]])%1000000007
  else:
    dp[i] = dp[i-1] 
  pos_dp[c[i]] = i

print(dp[n-1])