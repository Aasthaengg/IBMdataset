S = list(input())
N = len(S)
dp=[]
MOD = (10 ** 9) + 7
f = S.pop(0)
if f == '?':
  dp_low = [1,1,1,1,1,1,1,1,1,1,0,0,0]
else:
  dp_low = [0] * 13
  dp_low[int(f)] = 1
  
dp.append(dp_low)
for i in range(N-1):
  dp_low = [0] * 13
  if S[i] == '?':
    for j, val in enumerate(dp[i]):
      for k in range(10):
        temp = ((j * 10) + k) % 13
        dp_low[temp] += val
  else:
    for j, val in enumerate(dp[i]):
      temp = ((j * 10) + int(S[i])) % 13
      dp_low[temp] += val
  for i in range(13):
    dp_low[i] %= MOD
  dp.append(dp_low)
print(dp[-1][5])