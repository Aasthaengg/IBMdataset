n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
flag=[[True]*n for _ in range(n)]
for k in range(n):
  for i in range(n):
    for j in range(n):
      if i==j or j==k or k==i:
        continue
      if a[i][j]>a[i][k]+a[k][j]:
        print(-1)
        exit()
      if a[i][j]==a[i][k]+a[k][j]:
        flag[i][j]=False
        flag[j][i]=False
ans=0
for i in range(n-1):
  for j in range(i+1,n):
    if flag[i][j]:
      ans+=a[i][j]
print(ans)