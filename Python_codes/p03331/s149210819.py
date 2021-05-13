n=int(input())

ans=10**5
for a in range(1,n):
  b=n-a
  aa=list(str(a))
  bb=list(str(b))
  tmp=0
  for k in (aa+bb):
    tmp+=int(k)
  ans=min(ans,tmp)
print(ans)