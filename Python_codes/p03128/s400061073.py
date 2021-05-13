n,m = map(int,input().split())
a = list(map(int,input().split()))

d1 = {1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
d2 = {2:[1],3:[7],4:[4],5:[5,3,2],6:[9,6],7:[8]}

# dp[i]:i本のマッチを使用した場合の最大桁数
dp = [-float('inf') for _ in range(n+1)]
dp[0] = 0
for i in range(1,n+1):
  for ai in a:
    if i-d1[ai] >= 0:
      dp[i] = max(dp[i-d1[ai]]+1,dp[i])

a.sort(reverse = True)
ans = ''
r = n
k = dp[n]
while(r > 0):
  for ai in a:
    if r-d1[ai] >= 0 and dp[r-d1[ai]] == k-1:
      ans += str(ai)
      r -= d1[ai]
      k -= 1
      break

print(ans)
