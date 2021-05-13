MOD = 10**9+7
h, w, k = map(int, input().split())
ans = 0
dp = [ [0]*w for _ in range(h+1)]
dp[0][0] = 1
for i in range(h):
  for j in range(2**(w-1)):
    s = bin(j)[2:]
    s = "0"*(w-1-len(s)) + s
    for t in range(w-2):
      if s[t] == s[t+1] == "1":
        break
    else:
      s = "0" + s + "0"
      for t in range(w):
        if s[t] == "0" and s[t+1] == "0":
          dp[i+1][t] += dp[i][t]
        else:
          if s[t] == "1":
            dp[i+1][t] += dp[i][t-1]
          else:
            dp[i+1][t] += dp[i][t+1]
        dp[i+1][t] %= MOD
print(dp[h][k-1])