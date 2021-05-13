n,m,q=map(int,input().split())
a=[[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
  x,y=map(int,input().split())
  a[x-1][y-1]+=1
  
for j in range(n):
  for k in range(1,n):
    a[j][k]=a[j][k]+a[j][k-1]
    
for l in range(q):
  ans=0
  L,R=map(int,input().split())
  for g in range(L-1,R):
    ans+=a[g][R-1]
  print(ans)