m,k=map(int,input().split())
if 2**m<=k:print(-1);exit()
if m==1:
  if k==0:print(0,0,1,1)
  else:print(-1)
  exit()
a=[i for i in range(2**m) if i!=k]
ans=[k]+a+[k]+a[::-1]
print(*ans)
