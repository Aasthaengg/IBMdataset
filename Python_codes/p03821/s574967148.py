n=int(input())
a=[0]*n
b=[0]*n
for i in range(n):
  a[i],b[i]=map(int,input().split())
ans=0
for i in range(n-1,-1,-1):
  m=a[i]%b[i]
  if m:ans+=b[i]-m
  a[i-1]+=ans
print(ans)