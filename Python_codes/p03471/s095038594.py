n,y=map(int,input().split())
for i in range(2001):
  for j in range(2001):
    if i*9+j*4+n==y/1000 and i+j<=n:
      exit(print(i,j,n-i-j))
print(-1,-1,-1)