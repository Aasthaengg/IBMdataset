N=int(input())
S1=input()
S2=input()
mod=10**9+7
dp=[]
a=0
for i in range(N):
  if i!=N-1:
    if a==1:
      a=0
      continue
    else:
      if S1[i]==S1[i+1]:
        dp.append(2)
        a=1
      else:
        dp.append(1)
  else: 
    if a==0:
      dp.append(1)
ans=1
if len(dp)==1:
  if dp[0]==1:
    print(3)
  else:
    print(6)
  exit()
for i in range(len(dp)):
  if i==0:
    if dp[i]==1:
      ans*=3
    else:
      ans*=6
  else:
    if dp[i-1]==2:
      if dp[i]==1:
        continue
      else:
        ans*=3
    else:
      if dp[i]==1:
        ans*=2
      else:
        ans*=2
  ans%=mod
print(ans%mod)