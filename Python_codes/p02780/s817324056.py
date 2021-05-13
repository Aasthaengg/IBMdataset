n,k,*a=map(int,open(0).read().split())
b=[q+1 for q in a]
ans=sum(b[:k])
now=ans
for i in range(k,n):
  now=now+b[i]-b[i-k]
  ans=max(ans,now)
print(ans/2)