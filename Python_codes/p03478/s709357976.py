n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
  x=str(i)
  v=0
  for j in range(len(x)):
    v+=int(x[j])
  if a<=v<=b:
    ans+=i
print(ans)