N,A,B=map(int,input().split())
ans=0
for x in range(1,N+1):
  temp=0
  for y in str(x):
    temp+=int(y)
  else:
    if temp>=A and temp<=B:
      ans+=x
print(ans)