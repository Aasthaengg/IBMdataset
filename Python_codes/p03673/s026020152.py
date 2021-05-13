n=int(input())
a=list(map(int,input().split()))
dp=[0]*n
i,j,k=1,1,0
p=n//2
dp[p]=a[0]
if n%2==0:
  while i+j-1!=n:
    if k%2==0:
      dp[p-i]=a[i+j-1]
      i+=1
      k=1
    else:
      dp[p+j]=a[i+j-1]
      j+=1
      k=0
  print(*dp)
else:
  while i+j-1!=n:
    if k%2==0:
      dp[p+i]=a[i+j-1]
      i+=1
      k=1
    else:
      dp[p-j]=a[i+j-1]
      j+=1
      k=0
  print(*dp)