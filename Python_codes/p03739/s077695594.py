n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  if i!=0:
    a[i]=a[i]+a[i-1]
b=0
ans,bns=0,0
for i in range(n):
  if i%2==0:
    if a[i]+b>=0:
      ans+=(a[i]+1+b)
      b-=(a[i]+1+b)
  else:
    if a[i]+b<=0:
      ans+=(1-a[i]-b)
      b+=(1-a[i]-b)
b=0
for i in range(n):
  if i%2==0:
    if a[i]+b<=0:
      bns+=(1-a[i]-b)
      b+=(1-a[i]-b)
  else:
    if a[i]+b>=0:
      bns+=(a[i]+b+1)
      b-=(a[i]+b+1)
print(min(ans,bns))