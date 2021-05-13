n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
na=sorted(a)
nb=sorted(b)
c=[0]*n
for i in range(n):
  c[i]=a[i]-b[i]
if sum(c)<0:
  print(-1)
else:
  c.sort()
  ans=0
  s=0
  for i in range(n):
    if c[i]<0:
      s=s+abs(c[i])
      ans=ans+1
  for i in range(n):
    if s<=0:
      break
    else:
      s=s-c[n-i-1]
      ans=ans+1
  print(ans)