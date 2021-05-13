def solve():
  S = input()
  K = len(S)
  dp1 = [0]*(K+1)
  dp2 = [0]*(K+1)
  dp1[1] = 1
  dp2[2] = 1
  for i in range(1,K):
    dp1[i+1] = dp2[i]+1
    if S[i]!=S[i-1]:
      dp1[i+1] = max(dp1[i+1],dp1[i]+1)
    if i>=2:
      dp2[i+1] = dp1[i-1]+1
    if i>=3 and S[i-1:i+1]!=S[i-3:i-1]:
      dp2[i+1] = max(dp2[i+1],dp2[i-1]+1)
  ans = max(dp1[-1],dp2[-1])
  return ans
print(solve())