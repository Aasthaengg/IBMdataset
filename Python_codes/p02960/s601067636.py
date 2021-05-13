import copy
S = input()
S = S[::-1]
dp = [0 for _ in range(13)]
dp[0] = 1

mod = int(1e9+7)

def calc(dp,i,k):
  dpw = [0 for _ in range(13)]
  if S[i] == '?':
    X = [i for i in range(10)]
  else:
    X = [int(S[i])]
  for j in range(13):
    for x in X:
      dpw[(j+x*k)%13] += dp[j]  
      dpw[(j+x*k)%13] %= mod
  return dpw

keta = 1
for i in range(len(S)):
  dp = calc(dp,i,keta)
  keta = keta * 10 % 13

#print(dp)
print(dp[5])
#print(sum(dp))