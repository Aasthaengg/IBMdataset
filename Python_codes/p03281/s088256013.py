N=int(input())
ans=0
for x in range(1,N+1):
  if x%2==1:
    c=0
    for y in range(1,x+1):
      if x%y==0:
        c+=1
      if c>8:
        break
    if c==8:
      ans+=1
print(ans)