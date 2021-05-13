n,a,b=map(int,input().split())

ans=0
for i in range(1,n+1):
  count=0
  for j in str(i):
    count+=int(j)
  if a<=count<=b:
    ans+=i
print(ans)
