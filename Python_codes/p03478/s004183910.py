n,a,b=map(int,input().split())
k=0
ans=0
for i in range(1,n+1):
  for j in range(int(len(str(i)))):
    k+=int(str(i)[j])
  if a<=k<=b:
    ans+=i
  k=0
print(ans)
