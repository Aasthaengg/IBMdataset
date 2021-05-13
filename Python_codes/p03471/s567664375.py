n,y=map(int,input().split())
for i in range(n+1):
 for j in range(n-i+1):i*9+j*4+n==y/1e3<exit(print(i,j,n-i-j))
print(-1,-1,-1)