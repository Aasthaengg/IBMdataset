def solve():
  S = input()
  N = len(S)
  dp1,dp2 = [0]*(N+1),[0]*(N+1)
  dp1[1] = 1
  for i in range(2,N+1):
    dp1[i] = dp2[i-1]+1
    if S[i-1]!=S[i-2]:
      dp1[i] = max(dp1[i-1]+1,dp1[i])
    dp2[i] = dp1[i-2]+1
    if i<4 or S[i-2:i]!=S[i-4:i-2]:
      dp2[i] = max(dp2[i],dp2[i-2]+1)
  ans = max(dp1[-1],dp2[-1])
  return ans
print(solve())