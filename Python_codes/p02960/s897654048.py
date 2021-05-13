S = input()
MOD = 10 ** 9 + 7

# ある余りを10倍して13で割ったときの余りへの変換表
rests = [0] * 13
for i in range(len(rests)):
  rests[i] = i * 10 % 13
  
dp = [[0] * 13 for i in range(len(S))]

x0 = S[0]
if x0 != "?":
  dp[0][int(x0)] = 1
else:
  # ?の場合は0～9を全て取ることができ、その余りは0～9となる
  for i in range(10):
    dp[0][i] = 1

for i in range(1, len(dp)):
  x = S[i]
  if x != "?":
    x = int(x)
    # ?じゃない場合は、直前の各あまりをrestsで変換して、その数を足したところに数を代入する
    for j in range(len(dp[i - 1])):
      dp[i][(rests[j] + x) % 13] += dp[i - 1][j]
      dp[i][(rests[j] + x) % 13] %= MOD
  else:
    # ?は0～9の全てを取ることができる
    for j in range(len(dp[i - 1])):
      for k in range(10):
        dp[i][(rests[j] + k) % 13] += dp[i - 1][j]
        dp[i][(rests[j] + k) % 13] %= MOD
  
print(dp[-1][5])