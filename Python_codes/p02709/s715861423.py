n = int(input())
a = list(map(int,input().split()))

b = []
for i in range(n):
  b.append((a[i],i))
b.sort(reverse = True)

#dp[i][j]:(大きい順で)i番目まで見て、左に寄せたのがj個である場合の最大値

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
  x = b[i][0]
  y = b[i][1]
  for l in range(i+1):
    r = i-l
    dp[i+1][l+1] = max(dp[i+1][l+1],dp[i][l]+x*(y-l))
    dp[i+1][l] = max(dp[i+1][l],dp[i][l]+x*(n-1-r-y))

ans = 0
for i in range(n+1):
  ans = max(dp[n][i],ans)
print(ans)
#print(dp)