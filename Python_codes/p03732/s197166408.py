n,W = map(int, input().split())
wv = []
w1,v1 = map(int, input().split())
wv.append([0,v1])
for i in range(n-1):
  w,v = map(int, input().split())
  w -= w1
  wv.append([w,v])
dp = [[[-(10 ** 18)] * 301 for j in range(n+1)] for i in range(n+1)]
dp[0][0][0] = 0
for key,(wi,vi) in enumerate(wv):
  for num in range(key+1):
    for weight in range(3 * key + 1):
      dp[key+1][num][weight] = max(dp[key+1][num][weight],dp[key][num][weight])
      dp[key+1][num+1][weight+wi] = max(dp[key+1][num+1][weight+wi],dp[key][num][weight] + vi)
ans = 0
for k,i in enumerate(dp):
  for num,v in enumerate(i[:k+1]):
    res = W - num * w1
    if res < 0:
      continue
    ans = max(ans,max(v[:min(res+1,301)]))
print(ans)