import sys
s=int(input())
dp=[0]*1000001
dp[s]=1
cnt=1
for i in range(1000001):
  if s%2==1:
    s=3*s+1
  else:
    s//=2
  cnt+=1
  if dp[s]==1:
    print(cnt)
    sys.exit()
  else:
    dp[s]=1