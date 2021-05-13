L,R=map(int,input().split())
ans=10**12
for i in range(L,R):
  for j in range(i+1,R+1):
    a=(i*j)%2019
    if (a==0):
      print(0)
      exit()
    ans=min(ans,a)

print(ans)
