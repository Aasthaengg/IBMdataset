a=input()
n=len(a)
ans=n*(n-1)//2+1
d=dict()
for i in range(n):
  if a[i] not in d:
    d[a[i]]=1
  else:
    d[a[i]]+=1
d=list(d.items())
for i,j in d:
  ans-=j*(j-1)//2
print(ans)