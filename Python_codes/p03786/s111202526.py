n,*a=map(int,open(0).read().split())
a.sort()
s=[0]*n
s[0]=a[0]
for i in range(1,n):
  s[i]=s[i-1]+a[i]
ans=1
for i in range(1,n)[::-1]:
  if s[i-1]>=(a[i]+1)//2:
    ans+=1
  else:
    break
print(ans)