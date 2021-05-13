import sys
n=int(input())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
m=[0]*n
MOD=10**9+7
m[0]=t[0]
for i in range(1,n):
  if t[i-1]<t[i]:
    m[i]=t[i]
  else:
    m[i]=-1*t[i]
if m[n-1]>0 and m[n-1]!=a[n-1]:
  print(0)
  sys.exit()
if m[n-1]<0 and -1*m[n-1]<a[n-1]:
  print(0)
  sys.exit()
m[n-1]=a[n-1]
for i in range(n-2,-1,-1):
  if a[i+1]<a[i]:
    if (m[i]>0 and m[i]!=a[i]) or (m[i]<0 and -1*m[i]<a[i]):
      print(0)
      sys.exit()
    m[i]=a[i]
  else:
    m[i]=max(m[i],-1*a[i])
ans=1
for i in range(n):
  if m[i]<0:
    ans=(ans*-1*m[i])%MOD
print(ans)
