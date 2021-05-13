h,w,k = map(int, input().split())
mod = 10 ** 9 + 7
dp = [[0] * w for i in range(h+1)]
dp[0][0] = 1
b0,b1 = 1,0
c = [1]
for i in range(w-1):
  b0, b1 = b0+b1, b0
  c.append(b0+b1)
if w == 1:
  print(1)
  exit()
for i,v_i in enumerate(dp[:h]):
  for j,now in enumerate(v_i):
    if j == 0:
      dp[i+1][j] += (now * (c[max(0,w-2)])) % mod
      dp[i+1][j+1] += (now * (c[max(0,w-3)])) % mod
    elif j == w-1:
      dp[i+1][j] += (now * (c[max(0,w-2)])) % mod
      dp[i+1][j-1] += (now * (c[max(0,w-3)])) % mod
    else:
      dp[i+1][j-1] += (now * c[max(0,j-2)]*c[max(0,w-j-2)]) % mod
      dp[i+1][j] += (now * c[max(0,j-1)]*c[max(0,w-j-2)]) % mod
      dp[i+1][j+1] += (now * c[max(0,j-1)]*c[max(0,w-j-3)]) % mod
ans = dp[h][k-1] % mod
print(ans)