n,y=map(int,input().split())
count=0
for i in range(n+1):
  for j in range(n+1):
    k=n-i-j
    if k>=0 and k<=n:
      if i*10000+j*5000+k*1000==y:
        print(i,j,k)
        exit()
print(-1,-1,-1)