import sys
n=int(input())
t=list(map(int,input().split()))
a=list(map(int,input().split()))
ans=1
mod=10**9+7
if n==1:
  if t[0]==a[0]:
    print(1)
  else:
    print(0)
  sys.exit()
for i in range(n):
  if i==0:
    if a[i]>a[i+1]:
      if a[i]==t[i]:
        ans*=1
      else:
        ans*=0
    else:
      ans*=1
  elif i==n-1:
    if t[i-1]<t[i]:
      if a[i]==t[i]:
        ans*=1
      else:
        ans*=0
    else:
      ans*=1
  else:
    if t[i-1]<t[i] and a[i]==a[i+1]:
      if a[i]>=t[i]:
        ans*=1
      else:
        ans*=0
    elif t[i-1]==t[i] and a[i]>a[i+1]:
      if a[i]<=t[i]:
        ans*=1
      else:
        ans*=0
    elif t[i-1]<t[i] and a[i]>a[i+1]:
      if a[i]==t[i]:
        ans*=1
      else:
        ans*=0
    else:
      ans*=min(a[i],t[i])
  ans%=mod
print(ans)