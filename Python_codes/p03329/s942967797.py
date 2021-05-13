n=int(input())
dp=list(range(n+1))
dp[0]=0
a=[]
b=[]
i=1
while True:
  if 6**i>n:break
  a.append(6**i)
  i+=1
i=1
while True:
  if 9**i>n:break
  b.append(9**i)
  i+=1
for i in a:
  for j in range(i,n+1):
    dp[j]=min(dp[j],dp[j-i]+1)
for i in b:
  for j in range(i,n+1):
    dp[j]=min(dp[j],dp[j-i]+1)
print(dp[n])