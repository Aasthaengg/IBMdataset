n=input()
a=list(map(int,input().split()))
ans=10**18
for s in -1,1:
  c=0
  if a[0]*s<0:c=abs(s-a[0])
  elif a[0]*s>0:s=a[0]
  else:c=1
  for i in a[1:]:
    if s<0:
      b=-s+1
      c+=max(0,b-i)
      s+=max(i,b)
    else:
      b=-s-1
      c+=max(0,i-b)
      s+=min(i,b)
  ans=min(ans,c)
print(ans)