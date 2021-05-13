n,m,c=map(int,input().split())
b=list(map(int,input().split()))
a=[list(map(int,input().split())) for i in range(n)]

ans=0

for i in range(n):
  res=c
  for j in range(m):
    res+=a[i][j]*b[j]
  if res>0:
    ans+=1
print(ans)