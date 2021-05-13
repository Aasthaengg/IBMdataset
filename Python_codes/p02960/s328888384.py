s=input()
n=len(s)
arr=[]
cnt=0
mod=10**9+7
rem=[1,10,9,12,3,4]
for i in reversed(range(n)):
  if s[i]=='?':
    arr.append(rem[(n-i)%6-1])
  else:
    cnt+=rem[(n-i)%6-1]*int(s[i])
    cnt%=13
#print(arr)
#print(cnt)
if arr:
  m=len(arr)
  dp=[[0]*13 for _ in range(m)]
  for i in range(10):
    dp[0][i*arr[0]%13]+=1
  for i in range(1,m):
    for j in range(13):
      for k in range(10):
        dp[i][(k*arr[i]+j)%13]+=dp[i-1][j]
        dp[i][(k*arr[i]+j)%13]%=mod
  #print(dp)
  for i in range(13):
    if (cnt+i)%13==5:
      print(dp[m-1][i]%mod)
      exit()
else:
  if cnt==5:
    print(1)
  else:
    print(0)