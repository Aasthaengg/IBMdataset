n=int(input())
a=[0]*n
b=[0]*n
for i in range(n):
  at,bt=map(int,input().split())
  a[i]=at
  b[i]=bt
temp=0
for i in range(n):
  a[n-1-i]=a[n-1-i]+temp
  if a[n-1-i]%b[n-1-i]!=0:
    temp=temp+b[n-1-i]-a[n-1-i]%b[n-1-i]
print(temp)