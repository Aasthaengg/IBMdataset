n=int(input())
a=list(map(int,input().split()))
a.sort()
c=a[n-1]
if n==2:
  print(a[1],a[0])
  exit()
if c%2==0:
  p=c//2
  o=10**9
  for i in range(n):
    if abs(p-a[i])<=o:
      o=abs(p-a[i])
      ans=a[i]
else:
  p=c//2
  q=c//2+1
  o=10**9
  for i in range(n):
    if abs(p-a[i])<abs(q-a[i]):
      if abs(p-a[i])<o:
        o=abs(p-a[i])
        ans=a[i]
    else:
      if abs(q-a[i])<o:
        o=abs(q-a[i])
        ans=a[i]
print(c,ans)