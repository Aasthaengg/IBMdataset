n,k=map(int,input().split())
factorial=[1]
for i in range(1,2*n):
  factorial.append((factorial[i-1]*(i+1))%(10**9+7))
inv=[]
for i in range(n):
  inv.append(pow(factorial[i],10**9+5,10**9+7))
if k>=n-1:
  print((factorial[2*n-2]*inv[n-1]*inv[n-2])%(10**9+7))
else:
  ans=1
  for i in range (k):
    ans=(ans+factorial[n-1]*inv[i]*inv[n-i-2]*factorial[n-2]*inv[i]*inv[n-i-3])%(10**9+7)
  if k==1:
    ans-=1
  print(ans)
