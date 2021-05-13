N=int(input())
S=[input() for _ in range(N)]
S.sort()
S.append('0')
dp=[0]*5
for i in range(N+1):
  if i==N:
    continue
  if S[i]==S[i+1]:
    continue
  if S[i][0]=='M':
    dp[0]+=1
  elif S[i][0]=='A':
    dp[1]+=1
  elif S[i][0]=='R':
    dp[2]+=1
  elif S[i][0]=='C':
    dp[3]+=1
  elif S[i][0]=='H':
    dp[4]+=1
ans=0
for i in range(3):
  for j in range(i+1,4):
    for k in range(j+1,5):
      ans+=dp[i]*dp[j]*dp[k]
print(ans)