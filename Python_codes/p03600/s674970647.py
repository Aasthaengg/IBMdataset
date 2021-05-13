n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
b=[[j for j in i]for i in a]
c=[n*[1]for _ in range(n)]
for k in range(n):
  for i in range(n):
    for j in range(n):
      b[i][j]=min(b[i][j],b[i][k]+b[k][j])
      if a[i][j]==a[i][k]+a[k][j]:
        if i!=j and i!=k and j!=k:
          c[i][j]=0
if a!=b:exit(print(-1))
ans=0
for i in range(n):
  for j in range(i):
    if c[i][j]:ans+=a[i][j]
print(ans)