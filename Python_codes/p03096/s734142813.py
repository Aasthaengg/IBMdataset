import bisect
N = int(input())
MOD = pow(10,9)+7
C = []
dic = {}
for i in range(N):
  temp = int(input())
  C.append(temp)
  if temp not in dic:
    dic[temp] = [i]
  else:
    dic[temp].append(i)  
#print(C)
#print(dic)
dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(N):
  #print(dp)
  if i>= 1 and C[i] == C[i-1]:
    dp[i] = dp[i-1]
    continue
  if i >= 1:
    dp[i] += dp[i-1]%MOD
  #print(dp,i)
  color = C[i]
  temp = bisect.bisect_left(dic[color],i)
  if temp == 0:
    continue
  loc = dic[color][temp-1]
  #print(i,temp,dp[loc])
  dp[i] += dp[loc]%MOD
print(dp[-1]%MOD)