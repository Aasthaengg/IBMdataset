n, m = map(int, input().split())
dp = [0]*(n+1)
dp[0] = 1
m_list = [int(input()) for _ in range(m)]
for i in range(1,n+1):
  if i==1:
    if m_list and i==m_list[0]:
      m_list.pop(0)
      dp[i]=0
    else:
      dp[i]=1
  elif m_list and i == m_list[0]:
    m_list.pop(0)
    dp[i] = 0
  else:
    dp[i] = (dp[i-1]+dp[i-2])% 1000000007
print(dp[-1])